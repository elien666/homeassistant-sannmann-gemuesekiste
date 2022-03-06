from __future__ import annotations

import enum
from typing import TypedDict


class GemueseKiste(TypedDict):
    name: str
    this_week: str
    next_week: str


class Crate(enum.Enum):
    """Enum for allowed crates."""

    MIX_KLEIN = "Mixkiste klein"
    OBST_KLEIN = "Obstkiste klein"
    REGIONAL_KLEIN = "Regionalkiste klein"
    ROHKOST_KLEIN = "Rohkostkiste klein"
    SCHONKOST_KLEIN = "Schonkostkiste klein"
    UEBERRASCHUNG_KLEIN = "Überraschungskiste klein"
    BÜRO_KLEIN = "Bürokiste klein"
    SMOOTHIE_MITTEL = "Smoothiekiste mittel"
    BROT_DER_WOCHE = "Brot der Woche"
    KÄSE_DER_WOCHE = "Käse der Woche"
    WURST_DER_WOCHE = "Wurst der Woche"
    MIX_MITTEL = "Mixkiste mittel"
    OBST_MITTEL = "Obstkiste mittel"
    REGIONAL_MITTEL = "Regionalkiste mittel"
    ROHKOST_MITTEL = "Rohkostkiste mittel"
    SCHONKOST_MITTEL = "Schonkostkiste mittel"
    UEBERRASCHUNG_MITTEL = "Überraschungskiste mittel"
    BÜRO_MITTEL = "Bürokiste mittel"
    MIX_GROSS = "Mixkiste groß"
    OBST_GROSS = "Obstkiste groß"
    REGIONAL_GROSS = "Regionalkiste groß"
    ROHKOST_GROSS = "Rohkostkiste groß"
    SCHONKOST_GROSS = "Schonkostkiste groß"
    UEBERRASCHUNG_GROSS = "Überraschungskiste groß"
    BÜRO_GROSS = "Bürokiste groß"


CrateResults = dict[Crate, GemueseKiste]
