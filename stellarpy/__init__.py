"""
StellarPy
=========
An ambitious open-source ecosystem for space science, astronomy, orbital mechanics, 
rocketry, visualization, simulation, and AI-powered space analysis.
"""

from .astronomy import planet_info, Planet
from .orbital import orbital_period, escape_velocity
from .rocketry import delta_v

# Define public API exposed by the package
__all__ = [
    "planet_info", 
    "Planet", 
    "orbital_period", 
    "escape_velocity", 
    "delta_v"
]

__version__ = "0.1.0"