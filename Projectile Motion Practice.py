import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#Constants
g = 9.81 #Gravity
phi = 45
Cd = 0.5 # dimensionless
rho = 1 #Kg/m^3
A = 0.01 #m^2
#define the system for an ordinary differential equation
def projectile_motion(t, y):
    x, vx, y, vy = y #Unpacking the state variables
    dxdt = vx
    dvxdt = 0 #No acceleration due to gravity
    dydt = vy
    dvydt = -g  #Acceleration due to gravity
    return [dxdt, dvxdt, dydt, dvydt]
#The state vector y contains all the variables necessary to describe the motion at t
#Unpack: to access each state variable separately

#Initial conditions
xo, yo = 0, 0 #Initial position
vo = 20 #Initial speed (m/s)
theta = np.radians(phi) #angle in radians
vxo = vo * np.cos(theta) # Initial Velocity in X direction
vyo = vo * np.sin(theta) # Initial Velocity in Y direction

y_initial = [xo, vxo, yo, vyo]

#Define time span
t_span = (0, 2 * vyo / g) #time until projectile lands
t_eval = np.linspace(t_span[0], t_span[1], 100) #Time points for evaluation

#Solve using_ivp
solution = solve_ivp(projectile_motion, t_span, y_initial, t_eval = t_eval, method='RK45')

#Extract results
x_vals, y_vals = solution.y[0], solution.y[2] # position values

# Plot trajectory
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="Projectile Path")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.title("Projectile Motion using solve_ivp")
plt.legend()
plt.grid()
plt.show()



# Projectile motion with air resistance
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # Gravity (m/s^2)
phi = 30  # Launch angle (degrees)
Cd = 20  # Drag coefficient (dimensionless)
rho = 1  # Air density (kg/m^3)
A = 0.01  # Cross-sectional area (m^2)
m = 1  # Mass (kg)

# Define the system of ordinary differential equations
def projectile_motion(t, y):
    x, vx, y, vy = y  # Unpacking the state variables
    v = np.sqrt(vx**2 + vy**2)  # Speed
    dxdt = vx
    dvxdt = - (0.5 * Cd * rho * A * v * vx) / m
    dydt = vy
    dvydt = -g - (0.5 * Cd * rho * A * v * vy) / m  # Acceleration due to gravity with air resistance
    return [dxdt, dvxdt, dydt, dvydt]

# Initial conditions
x0, y0 = 0, 0  # Initial position (m)
v0 = 20  # Initial speed (m/s)
theta = np.radians(phi)  # Launch angle in radians
vx0 = v0 * np.cos(theta)  # Initial velocity in X direction (m/s)
vy0 = v0 * np.sin(theta)  # Initial velocity in Y direction (m/s)

y_initial = [x0, vx0, y0, vy0]

# Define time span
t_span = (0, 2 * vy0 / g)  # Time until projectile lands (s)
t_eval = np.linspace(t_span[0], t_span[1], 100)  # Time points for evaluation

# Solve using solve_ivp
solution = solve_ivp(projectile_motion, t_span, y_initial, t_eval=t_eval, method='RK45')

# Extract results
x_vals, y_vals = solution.y[0], solution.y[2]  # Position values

x_vals = x_vals[y_vals>=0]
y_vals = y_vals[y_vals>=0]

# Plot trajectory
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="Projectile Path With Air Resistance")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.title("Projectile Motion with Air Resistance using solve_ivp")
plt.legend()
plt.grid()
plt.show()


# Projectile motion with air resistance and Coriolis effect
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # Gravity (m/s^2)
phi = 30  # Launch angle (degrees)
Cd = 0.47  # Drag coefficient (dimensionless)
rho = 1.225  # Air density (kg/m^3)
A = 0.01  # Cross-sectional area (m^2)
m = 1  # Mass (kg)
omega = 1 # Earth's angular velocity (rad/s)
latitude = 45  # Latitude (degrees)

# Define the system of ordinary differential equations
def projectile_motion(t, y):
    x, vx, y, vy = y  # Unpacking the state variables
    v = np.sqrt(vx**2 + vy**2)  # Speed
    dxdt = vx
    dvxdt = - (0.5 * Cd * rho * A * v * vx) / m + 2 * omega * vy * np.sin(np.radians(latitude))
    dydt = vy
    dvydt = -g - (0.5 * Cd * rho * A * v * vy) / m - 2 * omega * vx * np.sin(np.radians(latitude))
    return [dxdt, dvxdt, dydt, dvydt]

# Initial conditions
x0, y0 = 0, 1000  # Initial position (m)
v0 = 20  # Initial speed (m/s)
theta = np.radians(phi)  # Launch angle in radians
vx0 = v0 * np.cos(theta)  # Initial velocity in X direction (m/s)
vy0 = v0 * np.sin(theta)  # Initial velocity in Y direction (m/s)

y_initial = [x0, vx0, y0, vy0]

# Define time span
t_span = (0, 2 * vy0 / g)  # Time until projectile lands (s)
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Time points for evaluation

# Solve using solve_ivp
solution = solve_ivp(projectile_motion, t_span, y_initial, t_eval=t_eval, method='RK45')

# Extract results
x_vals, y_vals = solution.y[0], solution.y[2]  # Position values

valid_indices = y_vals >= 0
x_vals = x_vals[valid_indices]
y_vals = y_vals[valid_indices]

# Plot trajectory
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="Projectile Path With Air Resistance and Coriolis Effect")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.title("Projectile Motion with Air Resistance and Coriolis Effect using solve_ivp")
plt.legend()
plt.grid()
plt.show()
