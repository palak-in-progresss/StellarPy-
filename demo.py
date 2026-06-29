from stellarpy import planet_info

# 1. Fetch information for Mars
mars = planet_info("Mars")

print("--- Mars Data ---")
print(f"Name: {mars.name}")
print(f"Mass: {mars.mass_kg} kg")
print(f"Radius: {mars.radius_m} m")
print(f"Gravity: {mars.gravity_mps2} m/s^2")
print(f"Number of Moons: {mars.number_of_moons}")
print(f"Orbital Period: {mars.orbital_period_s} seconds")
print(f"Rotation Period: {mars.rotation_period_s} seconds")

# 2. Test our error handling (seeking a non-existent planet)
try:
    print("\nAttempting to look up 'Krypton'...")
    planet_info("Krypton")
except ValueError as e:
    print("--- Error Caught Successfully! ---")
    print(e)