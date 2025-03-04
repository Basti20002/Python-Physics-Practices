#1-qubit states
import numpy as np
4
# Define |0⟩ and |1⟩ as column vectors
state_0 = np.array([[1], [0]])
state_1 = np.array([[0], [1]])

I = np.identity(2)
X = np.zeros((2, 2), dtype=complex)
X[0, 1] = 1 # Set element (0, 1) to 1
X[1, 0] = 1 # Set element (1, 0) to 1
Y = np.zeros((2, 2), dtype=complex)
Y[0, 1] = -1j
Y[1, 0] = 1j
Z = np.zeros((2, 2), dtype=complex)
Z[0, 0] = 1
Z[1, 1] = -1
5
#Rotation Gates
def Rx(theta):
    return np.array([[np.cos(theta / 2), -1j * np.sin(theta / 2)],
[-1j * np.sin(theta / 2), np.cos(theta / 2)]])
# Rotation angle θ (for example, 90 degrees or π/2 radians)
theta = np.pi / 2
# Apply the Identity Gate to the superposition state

# Coefficients for superposition
alpha = 1/np.sqrt(2)
beta = 1/np.sqrt(2)
# Create the superposition state |ψ⟩
superposition_state = alpha * state_0 + beta * state_1
# Print the superposition state
print(superposition_state)
new_state = np.dot(I, superposition_state)
# Apply the Pauli Gates to the superposition state
Xnew_state = np.dot(X, superposition_state)
Ynew_state = np.dot(Y, superposition_state)
Znew_state = np.dot(Z, superposition_state)
Inew_state = np.dot(I, superposition_state)
# Apply Rx to the superposition state
Rxnew_state = np.dot(Rx(theta), superposition_state)
print("Identity Gate:")
print(new_state)
print("X Gate:")
print(Xnew_state)
print("Y Gate:")
print(Ynew_state)
print("Z Gate:")
print(Znew_state)
print("Rx Gate:")
print(Rxnew_state)
print("Identity Gate")
print(Inew_state)