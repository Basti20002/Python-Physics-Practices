import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#Setting up parameters
Nx = 500 #Number of spatial points
L = 1.0 #length of string
dx = L / (Nx -1) #Step wise functions
c = 1.0 # wave speed

#creating spatial grid
x = np.linspace(0, L, Nx)

#Initial condition: Gaussian pulse at the center
u_initial = np.exp(-100 * (x-0.5)**2)
v_initial = np.zeros_like(x) #initial velocity is zero

y_initial = np.hstack([u_initial, v_initial])
#defining the wave function in first-order form
def wave_equation(t,y):
    u = y[:Nx] #Displacement ; First half of the array stores
    v = y[Nx:] #Velocity ; Second half of the array stores velocity
    dudt = v
    dvdt = np.zeros_like(v)
    #Finite difference method (central difference for second derivative)
    for i in range(1, Nx-1):
        dvdt[i] = c**2 * (u[i-1] - 2 *u[i] + u[i+1]) / dx**2
    return np.hstack([dudt, dvdt])
#Solve using solve_ivp
t_span = (0,1)
t_eval = np.linspace(0,1,100)
solution = solve_ivp(wave_equation, t_span, y_initial, t_eval=t_eval, method='RK45')

#Plotting the results
plt.figure(figsize=(8, 5))
for i in range(0, len(t_eval), 20): # Plot every 20th time step
    plt.plot(x, solution.y[Nx:, i], label=f"t = {t_eval[i]:.2f}", markersize=0.1)
plt.xlabel("Position x")
plt.ylabel("Displacement u(x,t)")
plt.title("Wave Equation Solution using solve_ivp")
plt.legend()
plt.show()


