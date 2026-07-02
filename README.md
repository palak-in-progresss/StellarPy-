# StellarPy 🌌

StellarPy is an open-source Python ecosystem designed for space science, astronomy, orbital mechanics, rocketry, visualization, and simulation. 

Rather than a simple educational script, StellarPy is built as a production-ready, typed, and fully tested library, serving as a foundation for students, researchers, and developers interested in space exploration.

---

## 🚀 Key Features

*   **Verified Planetary Database**: Query high-precision physical parameters (mass, radius, gravity, escape velocity, orbital/rotation periods) for all major planets in the Solar System.
*   **Dual-API Physics Engine**: 
    *   *Beginner-Friendly*: Compute orbital periods using altitudes and planet names (e.g., ISS around Earth).
    *   *Advanced*: Input custom semi-major axes and central masses to compute Keplerian orbits for arbitrary bodies.
*   **Rocketry Calculations**: Determine stage performance and Delta-V using the Tsiolkovsky Rocket Equation.
*   **Professional Engineering Standards**: 100% type-hinted, modular structure, and automated unit test suite.

---

## 🛠️ Installation & Setup

StellarPy is designed as a standard Python package. To install it locally in editable mode (great for development):

```bash
# Clone the repository
git clone https://github.com/palak-in-progresss/StellarPy-.git
cd StellarPy-

# Install package dependencies and dev tools
pip install -r requirements.txt
pip install -e .
```

---

## 💻 Quick Start Example

Run `demo.py` to see the library in action, or use it in your own scripts:

```python
from stellarpy import planet_info, orbital_period, escape_velocity, delta_v

# 1. Fetch planet data
mars = planet_info("Mars")
print(f"Mars surface gravity: {mars.gravity_mps2} m/s²")

# 2. Calculate orbital period (ISS around Earth at 400 km altitude)
period_seconds = orbital_period(altitude_m=400_000, central_body="Earth")
print(f"ISS Orbital Period: {period_seconds / 60.0:.2f} minutes")

# 3. Calculate escape velocity
v_esc = escape_velocity(radius_m=6_371_000, central_mass_kg=5.9722e24)
print(f"Earth Escape Velocity: {v_esc / 1000.0:.2f} km/s")

# 4. Calculate Rocket Delta-V
dv = delta_v(specific_impulse_s=300, mass_start_kg=10000, mass_dry_kg=3000)
print(f"Delta-V: {dv:.2f} m/s")
```

---

## 🧪 Running Automated Tests

We maintain strict test-driven development habits. To run the automated test suite (`pytest`):

```bash
pytest
```

Output:
```text
tests\test_astronomy.py ...                                              [ 30%]
tests\test_orbital.py .....                                              [ 80%]
tests\test_rocketry.py ..                                                [100%]
=========================== 10 passed in 0.38s ===========================
```

---

## 📐 Scientific Equations Utilized

### 1. Kepler's Third Law (Orbital Period)
$$T = 2\pi \sqrt{\frac{a^3}{GM}}$$
*   $T$ = Orbital period (seconds)
*   $a$ = Semi-major axis / orbit radius (meters)
*   $G$ = Gravitational constant ($6.6743 \times 10^{-11} \text{ m}^3\text{kg}^{-1}\text{s}^{-2}$)
*   $M$ = Mass of the central body (kg)

### 2. Escape Velocity
$$v_{esc} = \sqrt{\frac{2GM}{r}}$$
*   $v_{esc}$ = Escape velocity (m/s)
*   $r$ = Distance from the center of the body (meters)

### 3. Tsiolkovsky Rocket Equation (Delta-V)
$$\Delta v = I_{sp} \cdot g_0 \cdot \ln\left(\frac{m_0}{m_f}\right)$$
*   $\Delta v$ = Change in velocity (m/s)
*   $I_{sp}$ = Specific impulse (seconds)
*   $g_0$ = Standard gravity ($9.80665 \text{ m/s}^2$)
*   $m_0$ = Initial wet mass (kg)
*   $m_f$ = Final dry mass (kg)

---

## 🗺️ Roadmap
- [ ] **Visualization**: Orbit plotting utilities using `matplotlib` (elliptical orbits, Apoapsis/Periapsis markers).
- [ ] **Trajectory Analysis**: Hohmann transfer orbit calculations.
- [ ] **Data Integration**: Live telemetry fetching from NASA open APIs.
