"""
stellarpy.orbital
-----------------
Module containing core orbital mechanics calculations, including orbital periods
and escape velocities.
"""

import math
from typing import Optional
from stellarpy.data.constants import G_M3_KG_S2
from stellarpy.astronomy import planet_info

def orbital_period(
    *,
    altitude_m: Optional[float] = None,
    central_body: Optional[str] = None,
    semi_major_axis_m: Optional[float] = None,
    central_mass_kg: Optional[float] = None
) -> float:
    """
    Calculate the orbital period of a body in a circular or elliptical orbit.

    This function supports two modes of operation:
    1. Beginner API: Specify the orbit using 'altitude_m' and the 'central_body' name.
       Formula: semi_major_axis_m = central_body.radius_m + altitude_m
    2. Advanced API: Specify the orbit using 'semi_major_axis_m' and 'central_mass_kg'.

    Mathematical Formula:
        T = 2 * pi * sqrt( a^3 / (G * M) )
        where:
        T = Orbital period in seconds
        a = Semi-major axis (orbit radius) in meters
        G = Gravitational Constant
        M = Central mass in kg

    Args:
        altitude_m: The height of the orbit above the central body's surface in meters.
        central_body: Name of the central planetary body (e.g., "earth", "mars").
        semi_major_axis_m: The semi-major axis of the orbit in meters (distance from center).
        central_mass_kg: The mass of the central gravitational body in kg.

    Returns:
        float: The orbital period in seconds.

    Raises:
        ValueError: If parameters from the two modes are mixed, or if required parameters are missing.
    """
    # Mode 1: Beginner (altitude_m + central_body)
    if altitude_m is not None and central_body is not None:
        if semi_major_axis_m is not None or central_mass_kg is not None:
            raise ValueError(
                "Ambiguous arguments. Provide either (altitude_m AND central_body) OR "
                "(semi_major_axis_m AND central_mass_kg), but not both."
            )
        
        # Look up central body details from our database
        body = planet_info(central_body)
        a = body.radius_m + altitude_m
        M = body.mass_kg

    # Mode 2: Advanced (semi_major_axis_m + central_mass_kg)
    elif semi_major_axis_m is not None and central_mass_kg is not None:
        if altitude_m is not None or central_body is not None:
            raise ValueError(
                "Ambiguous arguments. Provide either (altitude_m AND central_body) OR "
                "(semi_major_axis_m AND central_mass_kg), but not both."
            )
        a = semi_major_axis_m
        M = central_mass_kg

    else:
        raise ValueError(
            "Invalid arguments. You must provide either:\n"
            "  1. 'altitude_m' AND 'central_body' (Beginner API)\n"
            "  2. 'semi_major_axis_m' AND 'central_mass_kg' (Advanced API)"
        )

    if a <= 0:
        raise ValueError("Orbit radius (semi-major axis) must be greater than zero.")
    if M <= 0:
        raise ValueError("Central body mass must be greater than zero.")

    # Calculate T = 2 * pi * sqrt( a^3 / (G * M) )
    return 2.0 * math.pi * math.sqrt((a ** 3) / (G_M3_KG_S2 * M))


def escape_velocity(radius_m: float, central_mass_kg: float) -> float:
    """
    Calculate the escape velocity from a central body at a given distance from its center.

    Mathematical Formula:
        v_esc = sqrt( (2 * G * M) / r )
        where:
        v_esc = Escape velocity in meters per second (m/s)
        G = Gravitational Constant
        M = Central mass in kg
        r = Distance from the center of the central body in meters

    Args:
        radius_m: The distance from the center of the central body in meters.
        central_mass_kg: The mass of the central body in kg.

    Returns:
        float: The escape velocity in meters per second (m/s).
    """
    if radius_m <= 0:
        raise ValueError("Radius must be greater than zero.")
    if central_mass_kg <= 0:
        raise ValueError("Central mass must be greater than zero.")

    return math.sqrt(2.0 * G_M3_KG_S2 * central_mass_kg / radius_m)