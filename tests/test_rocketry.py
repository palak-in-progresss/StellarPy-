import pytest
from stellarpy import delta_v

def test_delta_v_valid():
    # Specific impulse = 300 s, wet mass = 10,000 kg, dry mass = 3,000 kg
    # delta_v = 300 * 9.80665 * ln(10000 / 3000) = ~3542.08 m/s
    dv = delta_v(
        specific_impulse_s=300.0, 
        mass_start_kg=10000.0, 
        mass_dry_kg=3000.0
    )
    assert dv == pytest.approx(3542.08, rel=1e-4)

def test_delta_v_invalid():
    # Wet mass cannot be less than dry mass (you can't have negative fuel!)
    with pytest.raises(ValueError):
        delta_v(
            specific_impulse_s=300.0, 
            mass_start_kg=3000.0, 
            mass_dry_kg=10000.0
        )
    
    # Negative specific impulse is physically impossible
    with pytest.raises(ValueError):
        delta_v(
            specific_impulse_s=-10.0, 
            mass_start_kg=10000.0, 
            mass_dry_kg=3000.0
        )