from datetime import date
import logging

import aiohttp
from lxml import html

from .types import Crate, CrateResults

URL_PATTERN = "https://abo.sannmann.com/index.php5?l1=meinabo&l2=wocheninhalt&usrAbokiste={size}&usrJahr={year}&usrKalenderwoche={week}"
CRATE_SIZES = ["klein", "mittel", "gross"]

_LOGGER = logging.getLogger(__name__)


class FetchCrate:
    """Encapsulates logic for retrieving eshop sale data for countries."""

    def __init__(
        self,
        session: aiohttp.ClientSession,
    ) -> None:
        self.session = session
        today = date.today()
        self.current_week = today.isocalendar().week
        self.current_year = today.year

    async def fetch(self) -> CrateResults:
        """Fetch data about gemüsekisten."""

        result = {}
        for i in range(2):
            for size in CRATE_SIZES:
                url = (
                    URL_PATTERN.replace("{week}", str(self.current_week + i))
                    .replace("{size}", size)
                    .replace("{year}", str(self.current_year))
                )

                source = None

                async with self.session.get(url) as resp:
                    source = await resp.text()

                dom = html.fromstring(source)
                for enumeration in dom.xpath('//*[contains(@class, "aufzaehlung04")]'):
                    name = enumeration.xpath("./p/text()")[0]
                    lis = enumeration.xpath("./ul/li")
                    inner_html = ", ".join(
                        map(lambda li: li.xpath("string(.)").strip(), lis)
                    )
                    crate_name = Crate(name)
                    crate = (
                        result[crate_name] if crate_name in result else {"name": name}
                    )
                    crate["this_week" if i == 0 else "next_week"] = inner_html
                    result[crate_name] = crate

        return result
