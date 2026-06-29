"""
stellarpy.data.constants
------------------------
This module defines high-precision physical and astronomical constants
used throughout the StellarPy ecosystem. All constants are named with
explicit units to ensure scientific clarity.

References:
    - CODATA 2018 values for G and standard gravity.
    - IAU 2012 resolution for the Astronomical Unit (AU).
"""

# Gravitational Constant (m^3 kg^-1 s^-2)
# Reference: CODATA 2018
G_M3_KG_S2: float = 6.67430e-11

# Standard acceleration of gravity on Earth (m/s^2)
# Reference: CODATA 2018
G0_MPS2: float = 9.80665

# Astronomical Unit - mean distance from Earth to Sun (meters)
# Reference: IAU 2012 Resolution B2
AU_M: float = 149597870700.0