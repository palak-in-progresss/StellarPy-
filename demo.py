from stellarpy import planet_info, orbital_period, escape_velocity, delta_v

# 1. Fetch planetary info (Mars)
print("========================================")
print("1. QUERYING PLANETARY DATABASE")
print("========================================")
mars = planet_info("Mars")
print(f"Planet: {mars.name}")
print(f"Mass: {mars.mass_kg:.4e} kg")
print(f"Radius: {mars.radius_m:,.1f} m")
print(f"Surface Gravity: {mars.gravity_mps2:.3f} m/s^2")
print(f"Number of Moons: {mars.number_of_moons}")
print("")

# 2. Calculate Orbital Period (ISS around Earth - Beginner API)
print("========================================")
print("2. ORBITAL PERIOD CALCULATIONS")
print("========================================")
iss_altitude_m = 400_000.0  # 400 km
iss_period_s = orbital_period(altitude_m=iss_altitude_m, central_body="Earth")
iss_period_min = iss_period_s / 60.0

print("Beginner API (altitude + central body name):")
print(f"  ISS Orbital Period (at {iss_altitude_m/1000:.1f} km altitude):")
print(f"  {iss_period_s:.2f} seconds ({iss_period_min:.2f} minutes)")
print("")

# 3. Calculate Orbital Period (ISS around Earth - Advanced API)
# Using direct orbit radius (6371 km Earth radius + 400 km altitude = 6771 km) and Earth mass
iss_orbit_radius_m = 6_771_000.0
earth_mass_kg = 5.9722e24

iss_period_advanced_s = orbital_period(
    semi_major_axis_m=iss_orbit_radius_m, 
    central_mass_kg=earth_mass_kg
)
print("Advanced API (semi-major axis + central mass):")
print(f"  Orbital Period (using direct physical values):")
print(f"  {iss_period_advanced_s:.2f} seconds ({iss_period_advanced_s / 60.0:.2f} minutes)")
print("")

# 4. Calculate Escape Velocity (Earth Surface)
print("========================================")
print("3. ESCAPE VELOCITY CALCULATION")
print("========================================")
earth_escape_mps = escape_velocity(radius_m=6_371_000.0, central_mass_kg=5.9722e24)
earth_escape_kmps = earth_escape_mps / 1000.0
print(f"Earth Escape Velocity (at surface):")
print(f"  {earth_escape_mps:.2f} m/s ({earth_escape_kmps:.2f} km/s)")
print("")

# 5. Calculate Rocket Delta-V (Tsiolkovsky Rocket Equation)
print("========================================")
print("4. ROCKET PERFORMANCE (DELTA-V)")
print("========================================")
isp_s = 300.0          # Specific impulse in seconds (e.g. solid booster)
wet_mass_kg = 10_000.0 # Initial mass (fuel + rocket)
dry_mass_kg = 3_000.0  # Final mass (no fuel left)

dv_mps = delta_v(
    specific_impulse_s=isp_s, 
    mass_start_kg=wet_mass_kg, 
    mass_dry_kg=dry_mass_kg
)
print(f"Rocket Stage Performance:")
print(f"  Specific Impulse: {isp_s} seconds")
print(f"  Wet Mass: {wet_mass_kg:,.1f} kg")
print(f"  Dry Mass: {dry_mass_kg:,.1f} kg")
print(f"  Total Delta-V Achieved: {dv_mps:.2f} m/s")
print("========================================")