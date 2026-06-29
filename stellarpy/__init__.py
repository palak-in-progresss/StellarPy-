"""
StellarPy
=========
An ambitious open-source ecosystem for space science, astronomy, orbital mechanics, 
rocketry, visualization, simulation, and AI-powered space analysis.
"""

from .astronomy import planet_info, Planet

# Define public API exposed by the package
__all__ = ["planet_info", "Planet"]

__version__ = "0.1.0"