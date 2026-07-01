import pytest
from stellarpy import orbital_period, escape_velocity

def test_orbital_period_beginner():
    # Test Earth orbit at 400 km altitude (typical ISS orbit height)
    # Expected period: ~5544.46 seconds (about 92.4 minutes)
    period = orbital_period(altitude_m=400000.0, central_body="Earth")
    assert period == pytest.approx(5544.46, rel=1e-4)

def test_orbital_period_advanced():
    # Test using direct orbital radius and mass (Advanced API)
    # Orbit radius = Earth radius (6371 km) + 400 km altitude = 6771 km
    period = orbital_period(semi_major_axis_m=6771000.0, central_mass_kg=5.9722e24)
    assert period == pytest.approx(5544.46, rel=1e-4)

def test_orbital_period_ambiguous():
    # Mixing beginner and advanced arguments should raise ValueError
    with pytest.raises(ValueError):
        orbital_period(
            altitude_m=400000.0, 
            central_body="Earth", 
            central_mass_kg=5.9722e24
        )

def test_orbital_period_invalid():
    # Missing required arguments should fail
    with pytest.raises(ValueError):
        orbital_period(altitude_m=400000.0)
    
    # Zero or negative orbits/masses should fail
    with pytest.raises(ValueError):
        orbital_period(semi_major_axis_m=-1000.0, central_mass_kg=5.0e24)


def test_escape_velocity():
    # Escape velocity at Earth's surface (radius ~6371 km, mass ~5.9722e24 kg)
    # Expected: ~11186.86 m/s
    v_esc = escape_velocity(radius_m=6371000.0, central_mass_kg=5.9722e24)
    assert v_esc == pytest.approx(11186.86, rel=1e-4)