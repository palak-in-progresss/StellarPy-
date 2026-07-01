"""
stellarpy.rocketry
------------------
Module containing rocket performance calculations, including the Tsiolkovsky
rocket equation for delta-v.
"""

import math
from stellarpy.data.constants import G0_MPS2

def delta_v(
    specific_impulse_s: float, 
    mass_start_kg: float, 
    mass_dry_kg: float
) -> float:
    """
    Calculate the change in velocity (delta-v) using the Tsiolkovsky rocket equation.

    Mathematical Formula:
        delta_v = Isp * g0 * ln( m0 / mf )
        where:
        delta_v = change in velocity (m/s)
        Isp = specific impulse of the rocket engine (seconds)
        g0 = standard acceleration of gravity (9.80665 m/s^2)
        m0 = initial mass of the rocket (wet mass including fuel, kg)
        mf = final mass of the rocket (dry mass after fuel is consumed, kg)

    Args:
        specific_impulse_s: Specific impulse of the rocket engine in seconds.
        mass_start_kg: Initial wet mass of the spacecraft (including fuel) in kg.
        mass_dry_kg: Final dry mass of the spacecraft (after fuel is burned) in kg.

    Returns:
        float: The delta-v of the rocket stage in meters per second (m/s).

    Raises:
        ValueError: If any mass values are zero or negative, or if wet mass is 
                    less than dry mass.
    """
    if specific_impulse_s <= 0:
        raise ValueError("Specific impulse must be greater than zero.")
    if mass_start_kg <= 0:
        raise ValueError("Starting mass (wet mass) must be greater than zero.")
    if mass_dry_kg <= 0:
        raise ValueError("Dry mass must be greater than zero.")
    if mass_start_kg < mass_dry_kg:
        raise ValueError("Starting mass (wet mass) cannot be less than dry mass.")

    # Calculate delta-v: Isp * g0 * ln(m0 / mf)
    return specific_impulse_s * G0_MPS2 * math.log(mass_start_kg / mass_dry_kg)