import logging

from homeassistant import core
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)
from homeassistant.util import slugify

from .const import DOMAIN
from .types import Crate, CrateResults

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(
    hass: core.HomeAssistant, config, async_add_entities, discovery_info=None
) -> None:
    """Setup the sensor platform."""
    coordinator = hass.data[DOMAIN]["coordinator"]
    sensors = []
    for crate in coordinator.data.keys():
        sensors.append(GemueseKisteEntity(coordinator, crate))
    async_add_entities(sensors, True)
    # async_add_entities([GemueseKisteEntity(coordinator)], True)


class GemueseKisteEntity(CoordinatorEntity):
    """Representation of a sensor."""

    def __init__(
        self, coordinator: DataUpdateCoordinator[CrateResults], crate: str
    ) -> None:
        super().__init__(coordinator)
        self.attrs = {}
        self.crate = crate
        self._state = 0

    #    @property
    #    def unit_of_measurement(self):
    #        """Return the unit of measurement of this entity, if any."""
    #        return Undefined

    @property
    def icon(self):
        """Icon to use in the frontend."""
        return "mdi:fruit-grapes"

    @property
    def entity_id(self):
        """Return the entity id of the sensor."""
        slug = slugify(self.crate.name)
        return f"sensor.sannmann_gemuesekiste_{slug}"

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{self.crate.value} - Sannmann Gemüsekiste"

    @property
    def state(self):
        """Return the state of the sensor."""
        crate = self.coordinator.data[self.crate]
        if crate:
            self.attrs["name"] = crate["name"]
            self.attrs["this_week"] = crate["this_week"] if "this_week" in crate else ""
            self.attrs["next_week"] = crate["next_week"] if "next_week" in crate else ""
            return True

        return False

    @property
    def extra_state_attributes(self):
        return self.attrs
