import numpy as np
import matplotlib.pyplot as plt
# Lattice size
L = 20 # 20x20 grid
num_electrons = 100 # Number of electrons
num_steps = 20 # Steps per electron
E_field_strength = 0.2 # Stronger electric field bias
# Initialize electron positions (start at the center of the lattice)
center = L // 2
electrons = np.full((num_electrons, 2), center)
# Define possible moves: [Right, Left, Down, Up]
moves = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
# Effect of E field
base_prob = 1.0
prob_left = base_prob/4 + E_field_strength
prob_right = max(0, base_prob/4 - E_field_strength) # Ensure no negative probability
prob_up = base_prob/4
prob_down = base_prob/4
# Normalize probabilities
probabilities = np.array([prob_right, prob_left, prob_up, prob_down])
probabilities /= probabilities.sum() # Ensure sum = 1
# Monte Carlo Simulation
for i in range(num_electrons):
	for _ in range(num_steps):
		step = moves[np.random.choice(4, p=probabilities)] # Weighted random move
		electrons[i] += step # Move electron
		electrons[i] = electrons[i] % L # Apply periodic boundary conditions
# Extract final positions of all electrons
x_positions, y_positions = electrons[:, 0], electrons[:, 1]
# Count electrons on the left and right of the center
num_right = np.sum(x_positions > center)
num_left = np.sum(x_positions < center)
# Plot the lattice with electron positions
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
# 1. Scatter plot of final electron positions
ax[0].grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
# Draw lattice points
for x in range(L):
	for y in range(L):
		ax[0].scatter(x - center, y - center, color='lightgray', s=10) # Lattice sites
# Plot electron positions (centered at origin)
ax[0].scatter(x_positions - center, y_positions - center, color='blue', s=50,
label="Electrons")
# Mark the center of the lattice
ax[0].scatter(0, 0, color='red', s=100, label="Lattice Center", edgecolors='black')
ax[0].set_xlim(-10, 10)
ax[0].set_ylim(-10, 10)
ax[0].set_xticks(range(-10, 11, 5))
ax[0].set_yticks(range(-10, 11, 5))
ax[0].set_title("Monte Carlo Electron Transport on a 2D Lattice\n(Strong Electric Field in +X Direction)")
ax[0].set_xlabel("X Position (Shifted)")
ax[0].set_ylabel("Y Position (Shifted)")
ax[0].legend()
# 2. Display total electrons on left and right
ax[1].axis('off') # Hide axis
ax[1].text(0.5, 0.7, f"Electrons Right of Center: {num_right}", fontsize=14, color='blue',
ha='center')
ax[1].text(0.5, 0.5, f"Electrons Left of Center: {num_left}", fontsize=14, color='red',
ha='center')
ax[1].set_title("Total Electrons on Left and Right")
plt.show()


