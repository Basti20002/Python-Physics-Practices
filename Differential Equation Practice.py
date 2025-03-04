import sympy as sp
from sympy.physics.mechanics import kinetic_energy
from sympy.physics.units import acceleration

#Define the symbols used for this example
t = sp.symbols('t') #Time variable
x = sp.Function('x')(t) #Displacement as a func of time
#Parameters and initicla conditions
m, gamma, k, Fo, omega, xo, vo, I = sp.symbols('m gamma k Fo omega xo vo I')

#Differential Equation for SHM oscillator:
eq = sp.Eq(m * x.diff(t, t) + k * x, 0)
#m d^2x/dx^2 + k * x = 0 is what we are doing
eq2 = sp.Eq(m * x.diff(t, t) + gamma * x.diff(t) + k *x, 0)
#m d^2x/dx^2 + gamma * dx/dt + kx = 0 is what we are doing for the damped harmonic oscillator
eq3 = sp.Eq(m * x.diff(t, t) + gamma * x.diff(t) + k *x, Fo * sp.cos(omega * t))
#m d^2x/dx^2 + gamma * dx/dt + kx = Fo* cos(omega*t) is what we are doing for the forced harmonic oscillator

#initial conditions
initial_conditions = {x.subs(t, 0): xo, x.diff(t).subs(t, 0): vo}

#Solving this differential Equations
solutions_with_ic = sp.dsolve(eq, ics=initial_conditions)
solutions_with_ic2 = sp.dsolve(eq2, ics=initial_conditions)
solutions_with_ic3 = sp.dsolve(eq3, ics=initial_conditions)
#Displaying the solution
print(f"Solutions with IC Simple Harmonic Oscillations: {solutions_with_ic}")

print(f"Solutions with IC Damped Harmonic Oscillation: {solutions_with_ic2}")

print(f"Solutions with IC Forced Harmonic Oscillations: {solutions_with_ic3}")





#Now lets do this with a numerical solution

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def SHO(y, t, m, k):
    x,v = y #Unpacking position and velocity
    dxdt = v #dx/dt = velocity
    dvdt = -k * x/ m #dv/dt = acceleration (In this case F = ma = -kx )
    return (dxdt, dvdt)

#Parameters
m = 1.0 #Kg
k = 1.0 #(N/m)
xo = 1.0 #m
vo = 0.0 #(m/s)
#Inital Conditions [initial position, initial velocity]
yo = [xo, vo]
#Time points where solution is computed
t = np.linspace(0,20,500)
solution = spi.odeint(SHO, yo, t, args=(m, k))
#extract solution
position = solution[:, 0]
velocity = solution[:, 1]
#calculating energies
kineticE = 0.5 * m * velocity**2
potentialE = 0.5 * k * position**2
#This needs to be constant
totalE = kineticE + potentialE

acceleration = -k * position / m

# Plot results
plt.figure(figsize=(10, 6))
# Plot position vs. time
plt.subplot(4, 1, 1)
plt.plot(t, position, label='Position (x)', color='b')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Simple Harmonic Oscillator: Position vs Time')
plt.grid(True)
plt.legend()
# Plot velocity vs. time
plt.subplot(4, 1, 2)
plt.plot(t, velocity, label='Velocity (v)', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Simple Harmonic Oscillator: Velocity vs Time')
plt.grid(True)
plt.legend()
# Plot acceleration vs. time
plt.subplot(4, 1, 3)
plt.plot(t, acceleration, label='Acceleration (a)', color='g')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Simple Harmonic Oscillator: Acceleration vs Time')
plt.grid(True)
plt.legend()
# Plot energies vs. time
plt.subplot(4, 1, 4)
plt.plot(t, kineticE, label='Kinetic Energy (KE)', color='g')
plt.plot(t, potentialE, label='Potential Energy (PE)',
color='orange')
plt.plot(t, totalE, label='Total Energy (E)', color='purple',
linestyle='dashed')
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.title('Simple Harmonic Oscillator: Energies vs Time')
plt.grid(True)
plt.legend()
# Show the plots
plt.tight_layout()
plt.show()



#IVP is the better method so use this in the future

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
# Define the SHO differential equation
def sho(t, y, m, k):
    x, v = y  # Unpacking position and velocity
    dxdt = v  # dx/dt = velocity
    dvdt = -k * x / m  # dv/dt = acceleration (In this case F = ma = -kx )
    return [dxdt, dvdt]
# Parameters
m = 1.0 # Mass (kg)
k = 1.0 # Spring constant (N/m)
x0 = 1.0 # Initial position (m)
v0 = 0.0 # Initial velocity (m/s)
# Initial conditions [initial position, initial velocity]
y0 = [x0, v0]
# Time span for the solution (start, end)
t_span = (0, 20)
# Time points where solution is computed
t_eval = np.linspace(0, 20, 500)
# Solve the differential equation using solve_ivp
solution = solve_ivp(sho, t_span, y0, args=(m, k), t_eval=t_eval)
# Extract solution
time = solution.t
position = solution.y[0]
velocity = solution.y[1]
# Calculate energies
kinetic_energy = 0.5 * m * velocity**2
potential_energy = 0.5 * k * position**2
total_energy = kinetic_energy + potential_energy # Should be constant
#for SHO
acceleration = -k * position / m
# Plot results
plt.figure(figsize=(10, 6))
# Plot position vs. time
plt.subplot(4, 1, 1)
plt.plot(time, position, label='Position (x)', color='b')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Simple Harmonic Oscillator: Position vs Time')
plt.grid(True)
plt.legend()
# Plot velocity vs. time
plt.subplot(4, 1, 2)
plt.plot(time, velocity, label='Velocity (v)', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Simple Harmonic Oscillator: Velocity vs Time')
plt.grid(True)
plt.legend()
# Plot a vs. time
plt.subplot(4, 1, 3)
plt.plot(time, acceleration, label='Acceleration (a)', color='g')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Simple Harmonic Oscillator: Acceleration vs Time')
plt.grid(True)
plt.legend()
# Plot energies vs. time
plt.subplot(4, 1, 4)
plt.plot(time, kinetic_energy, label='Kinetic Energy (KE)', color='g')
plt.plot(time, potential_energy, label='Potential Energy (PE)',
color='orange')
plt.plot(time, total_energy, label='Total Energy (E)', color='purple',
linestyle='dashed')
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.title('Simple Harmonic Oscillator: Energies vs Time')
plt.grid(True)
plt.legend()
# Show the plots
plt.tight_layout()
plt.show()



#Damped Oscillator version
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the damped SHO differential equation
def damped_sho(t, y, m, gamma, k):
    x, v = y  # Unpacking position and velocity
    dxdt = v  # dx/dt = velocity
    dvdt = -gamma * v / m - k * x / m  # dv/dt = acceleration (In this case F = ma = -gamma*v - kx)
    return [dxdt, dvdt]

# Parameters
m = 1.0  # Mass (kg)
gamma = 0.1  # Damping coefficient (kg/s)
k = 1.0  # Spring constant (N/m)
x0 = 1.0  # Initial position (m)
v0 = 0.0  # Initial velocity (m/s)

# Initial conditions [initial position, initial velocity]
y0 = [x0, v0]

# Time span for the solution (start, end)
t_span = (0, 20)

# Time points where solution is computed
t_eval = np.linspace(0, 20, 500)

# Solve the differential equation using solve_ivp
solution = solve_ivp(damped_sho, t_span, y0, args=(m, gamma, k), t_eval=t_eval)

# Extract solution
time = solution.t
position = solution.y[0]
velocity = solution.y[1]

# Calculate energies
kinetic_energy = 0.5 * m * velocity**2
potential_energy = 0.5 * k * position**2
total_energy = kinetic_energy + potential_energy  # Should decrease over time due to damping

# Calculate acceleration
acceleration = -gamma * velocity / m - k * position / m

# Plot results
plt.figure(figsize=(10, 8))

# Plot position vs. time
plt.subplot(4, 1, 1)
plt.plot(time, position, label='Position (x)', color='b')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Damped Harmonic Oscillator: Position vs Time')
plt.grid(True)
plt.legend()

# Plot velocity vs. time
plt.subplot(4, 1, 2)
plt.plot(time, velocity, label='Velocity (v)', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Damped Harmonic Oscillator: Velocity vs Time')
plt.grid(True)
plt.legend()

# Plot acceleration vs. time
plt.subplot(4, 1, 3)
plt.plot(time, acceleration, label='Acceleration (a)', color='g')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Damped Harmonic Oscillator: Acceleration vs Time')
plt.grid(True)
plt.legend()

# Plot energies vs. time
plt.subplot(4, 1, 4)
plt.plot(time, kinetic_energy, label='Kinetic Energy (KE)', color='g')
plt.plot(time, potential_energy, label='Potential Energy (PE)', color='orange')
plt.plot(time, total_energy, label='Total Energy (E)', color='purple', linestyle='dashed')
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.title('Damped Harmonic Oscillator: Energies vs Time')
plt.grid(True)
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()




# Forced Oscillator version
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sympy as sp

# Define symbols
t = sp.symbols('t')
x = sp.Function('x')(t)

# Define the differential equation
m = 1.0  # Mass (kg)
gamma = 0.1  # Damping coefficient (kg/s)
k = 2.0  # Spring constant (N/m)
Fo = 1.0
omega = (k * m)**(1/2)

eq3 = sp.Eq(m * x.diff(t, t) + gamma * x.diff(t) + k * x, Fo * sp.cos(omega * t))

# Define the damped SHO differential equation
def forced_sho(t, y, m, gamma, k, Fo, omega):
    x, v = y  # Unpacking position and velocity
    dxdt = v  # dx/dt = velocity
    dvdt = -gamma * v / m - k * x / m + Fo * np.cos(omega * t)  # dv/dt = acceleration
    return [dxdt, dvdt]

# Initial conditions [initial position, initial velocity]
x0 = 1.0  # Initial position (m)
v0 = 0.0  # Initial velocity (m/s)
y0 = [x0, v0]

# Time span for the solution (start, end)
t_span = (0, 20)

# Time points where solution is computed
t_eval = np.linspace(0, 20, 500)

# Solve the differential equation using solve_ivp
solution = solve_ivp(forced_sho, t_span, y0, args=(m, gamma, k, Fo, omega), t_eval=t_eval)

# Extract solution
time = solution.t
position = solution.y[0]
velocity = solution.y[1]

# Calculate energies
kinetic_energy = 0.5 * m * velocity**2
potential_energy = 0.5 * k * position**2
total_energy = kinetic_energy + potential_energy  # Should decrease over time due to damping

# Calculate acceleration
acceleration = -gamma * velocity / m - k * position / m + Fo * np.cos(omega * t_eval)

# Plot results
plt.figure(figsize=(10, 8))

# Plot position vs. time
plt.subplot(4, 1, 1)
plt.plot(time, position, label='Position (x)', color='b')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Forced Harmonic Oscillator: Position vs Time')
plt.grid(True)
plt.legend()

# Plot velocity vs. time
plt.subplot(4, 1, 2)
plt.plot(time, velocity, label='Velocity (v)', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Forced Harmonic Oscillator: Velocity vs Time')
plt.grid(True)
plt.legend()

# Plot acceleration vs. time
plt.subplot(4, 1, 3)
plt.plot(time, acceleration, label='Acceleration (a)', color='g')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Forced Harmonic Oscillator: Acceleration vs Time')
plt.grid(True)
plt.legend()

# Plot energies vs. time
plt.subplot(4, 1, 4)
plt.plot(time, kinetic_energy, label='Kinetic Energy (KE)', color='g')
plt.plot(time, potential_energy, label='Potential Energy (PE)', color='orange')
plt.plot(time, total_energy, label='Total Energy (E)', color='purple', linestyle='dashed')
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.title('Forced Harmonic Oscillator: Energies vs Time')
plt.grid(True)
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()