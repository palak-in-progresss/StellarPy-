"""
stellarpy.data.planets
----------------------
High-precision registry of planetary parameters for the 8 major planets in
the Solar System. All units are explicitly defined in the parameter keys.

Source:
    NASA Planetary Fact Sheets (https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
"""

from typing import Dict, Any

PLANET_DATABASE: Dict[str, Dict[str, Any]] = {
    "mercury": {
        "name": "Mercury",
        "mass_kg": 3.3011e23,
        "radius_m": 2439700.0,
        "gravity_mps2": 3.7,
        "escape_velocity_mps": 4250.0,
        "surface_temperature_k": 340.0,
        "number_of_moons": 0,
        "rotation_period_s": 5066976.0,
        "orbital_period_s": 7600521.6,
    },
    "venus": {
        "name": "Venus",
        "mass_kg": 4.8675e24,
        "radius_m": 6051800.0,
        "gravity_mps2": 8.87,
        "escape_velocity_mps": 10360.0,
        "surface_temperature_k": 737.0,
        "number_of_moons": 0,
        "rotation_period_s": -20997187.2,  # Negative denotes retrograde rotation
        "orbital_period_s": 19414166.4,
    },
    "earth": {
        "name": "Earth",
        "mass_kg": 5.9722e24,
        "radius_m": 6371000.0,
        "gravity_mps2": 9.807,
        "escape_velocity_mps": 11186.0,
        "surface_temperature_k": 288.0,
        "number_of_moons": 1,
        "rotation_period_s": 86164.1,      # Sidereal day
        "orbital_period_s": 31558149.5,    # Sidereal year
    },
    "mars": {
        "name": "Mars",
        "mass_kg": 6.4171e23,
        "radius_m": 3389500.0,
        "gravity_mps2": 3.711,
        "escape_velocity_mps": 5027.0,
        "surface_temperature_k": 210.0,
        "number_of_moons": 2,
        "rotation_period_s": 88642.7,
        "orbital_period_s": 59355072.0,
    },
    "jupiter": {
        "name": "Jupiter",
        "mass_kg": 1.8982e27,
        "radius_m": 69911000.0,
        "gravity_mps2": 24.79,
        "escape_velocity_mps": 59500.0,
        "surface_temperature_k": 165.0,
        "number_of_moons": 95,
        "rotation_period_s": 35729.9,
        "orbital_period_s": 374335776.0,
    },
    "saturn": {
        "name": "Saturn",
        "mass_kg": 5.6834e26,
        "radius_m": 58232000.0,
        "gravity_mps2": 10.44,
        "escape_velocity_mps": 35500.0,
        "surface_temperature_k": 134.0,
        "number_of_moons": 146,
        "rotation_period_s": 38362.5,
        "orbital_period_s": 929596608.0,
    },
    "uranus": {
        "name": "Uranus",
        "mass_kg": 8.6810e25,
        "radius_m": 25362000.0,
        "gravity_mps2": 8.69,
        "escape_velocity_mps": 21300.0,
        "surface_temperature_k": 76.0,
        "number_of_moons": 28,
        "rotation_period_s": -62063.7,     # Retrograde rotation
        "orbital_period_s": 2651486400.0,
    },
    "neptune": {
        "name": "Neptune",
        "mass_kg": 1.0241e26,
        "radius_m": 24622000.0,
        "gravity_mps2": 11.15,
        "escape_velocity_mps": 23500.0,
        "surface_temperature_k": 72.0,
        "number_of_moons": 16,
        "rotation_period_s": 57996.0,
        "orbital_period_s": 5200000000.0,
    }
}