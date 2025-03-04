import numpy as np
import matplotlib.pyplot as plt
# Parameters
m = 1 #mass
k = 4.0 * np.pi**2 #coefficient
A = 1.0 # Amplitude
omega = 2.0 * np.pi # Angular frequency
phi = 0.0 # Phase angle
t = np.arange(0, 8, 0.04) # Time values
# Displacement equation
x = A * np.cos(omega * t + phi)
# Velocity equation
v = -A * omega * np.sin(omega * t + phi)
# Acceleration equation
a = -A * (omega**2)*np.cos(omega * t + phi)
# Calculate energies
kinetic_energy = 0.5 * m * v**2
potential_energy = 0.5 * k * x**2
total_energy = kinetic_energy + potential_energy # Should be constant for SHO
# Plot results
plt.figure(figsize=(10, 6))
# Plot position vs. time
plt.subplot(2,2,1)
plt.plot(t, x, label='Position (x)', color='b')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Simple Harmonic Oscillator: Position vs Time')
plt.grid(True)
plt.legend()
# Plot velocity vs. time
plt.subplot(2,2,2)
plt.plot(t, v, label='Velocity (v)', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Simple Harmonic Oscillator: Velocity vs Time')
plt.grid(True)
plt.legend()
# Plot a vs. time
plt.subplot(2, 2, 3)
plt.plot(t, a, label='Acceleration (a)', color='g')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Simple Harmonic Oscillator: Acceleration vs Time')
plt.grid(True)
plt.legend()
# Plot energies vs. time
plt.subplot(2, 2, 4)
plt.plot(t, kinetic_energy, label='Kinetic Energy (KE)', color='g')
plt.plot(t, potential_energy, label='Potential Energy (PE)', color='orange')
plt.plot(t, total_energy, label='Total Energy (E)', color='purple', linestyle='dashed')
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.title('Simple Harmonic Oscillator: Energies vs Time')
plt.grid(True)
plt.legend()
# Show the plots
plt.tight_layout()
plt.show()