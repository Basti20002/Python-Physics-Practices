import numpy as np
import matplotlib.pyplot as plt
# Lattice parameters
L = 10 # Number of atoms in each row/column
a = 1.0 # Lattice constant (distance between atoms)
# Generate grid of points
x = np.arange(0, L * a, a)
y = np.arange(0, L * a, a)
X, Y = np.meshgrid(x, y)
# Flatten the arrays for plotting
x_positions = X.flatten()
y_positions = Y.flatten()
# Plot the square lattice
plt.figure(figsize=(6,6))
plt.scatter(x_positions, y_positions, s=200, color='blue', edgecolors='black',
label="Atoms")
plt.title("Square Lattice of Atoms")
plt.xlabel("X Position (Å)")
plt.ylabel("Y Position (Å)")
plt.xlim(-a, L*a) # Set limits with some padding
plt.ylim(-a, L*a)
plt.gca().set_aspect('equal') # Keep aspect ratio square
#plt.legend()
plt.grid(True, linestyle="--", alpha=1)
# Set custom tick spacing
plt.xticks(np.arange(0, L * a + 1, 1 * a)) # Major grid every 2 units
plt.yticks(np.arange(0, L * a + 1, 1 * a))
#plt.show()

#######
#Electrion Transport Random Walk


L = 20 # 20x20 grid
num_electrons = 100 # Number of electrons
num_steps = 500 # Steps per electron
# Initialize electron positions (start at the center of the lattice)
center =  L / 2

electrons = np.full((num_electrons, 2), center)
# Define possible moves: up, down, left, right
moves = np.array([[0, 1], [0, -1], [1, 0], [-1, 0]])
# Monte Carlo Simulation
for i in range(num_electrons):
    for _ in range(num_steps):
        step = moves[np.random.randint(0, 4)] # Pick a random direction
        electrons[i] += step # Move electron
        # Apply periodic boundary conditions (electron wraps around edges)
        electrons[i] = (electrons[i] + L) % L - L / 2
# Extract final positions of all electrons
x_positions, y_positions = electrons[:, 0], electrons[:, 1]
# Plot the lattice
plt.figure(figsize=(6,6))
plt.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
# Draw lattice points
for x in range(-L//2, L//2 + 1):
    for y in range(-L//2, L//2 + 1):
        plt.scatter(x, y, color='lightgray', s=10) # Lattice sites
# Plot electron positions
plt.scatter(x_positions, y_positions, color='blue', s=50, label="Electrons")
# Mark the center of the lattice
plt.scatter(0, 0, color='red', s=100, label="Lattice Center", edgecolors='black')
plt.xlim(-L//2, L//2)
plt.ylim(-L//2, L//2)
plt.xticks(range(-L//2, L//2 + 1))
plt.yticks(range(-L//2, L//2 + 1))
plt.title("Monte Carlo Electron Transport on a 2D Lattice")
plt.xlabel("X Position")
plt.ylabel("Y Position")
#plt.legend()
plt.show()