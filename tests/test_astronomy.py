import pytest
from stellarpy import planet_info, Planet

def test_planet_info_valid():
    # Verify that we can fetch Mars and get correct types and values
    mars = planet_info("Mars")
    assert isinstance(mars, Planet)
    assert mars.name == "Mars"
    assert mars.number_of_moons == 2
    assert mars.mass_kg == 6.4171e23

def test_planet_info_case_insensitive():
    # Verify case insensitivity and whitespace stripping
    earth_lower = planet_info("earth")
    earth_spaced = planet_info("  EARTH  ")
    assert earth_lower.name == "Earth"
    assert earth_lower == earth_spaced

def test_planet_info_invalid():
    # Verify that searching for a non-existent planet raises a ValueError
    with pytest.raises(ValueError) as excinfo:
        planet_info("Krypton")
    assert "Planet 'Krypton' not found" in str(excinfo.value)