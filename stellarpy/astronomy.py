"""
stellarpy.astronomy
-------------------
Core astronomy module for querying celestial body information and performing
general planetary calculations.
"""

from dataclasses import dataclass
from stellarpy.data.planets import PLANET_DATABASE

@dataclass(frozen=True)
class Planet:
    """
    Data class representing physical and orbital characteristics of a planet.
    All properties are read-only and explicitly suffixed with their physical units.
    """
    name: str
    mass_kg: float
    radius_m: float
    gravity_mps2: float
    escape_velocity_mps: float
    surface_temperature_k: float
    number_of_moons: int
    rotation_period_s: float
    orbital_period_s: float

def planet_info(name: str) -> Planet:
    """
    Retrieve verified physical and orbital characteristics for a planet in the Solar System.

    Args:
        name: The name of the planet (case-insensitive, e.g., "Mars" or "mars").

    Returns:
        Planet: A read-only dataclass containing the planet's characteristics.

    Raises:
        ValueError: If the planet name is not found in the database.
    """
    lookup_key = name.strip().lower()
    
    if lookup_key not in PLANET_DATABASE:
        available = ", ".join(sorted([p.capitalize() for p in PLANET_DATABASE.keys()]))
        raise ValueError(
            f"Planet '{name}' not found in database. "
            f"Available options: {available}"
        )
    
    # Unpack the dictionary parameters into the Planet dataclass
    planet_data = PLANET_DATABASE[lookup_key]
    return Planet(**planet_data)