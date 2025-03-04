import numpy as np
# Define the basic 1-qubit states
state_0 = np.array([1, 0]) # |0⟩
state_1 = np.array([0, 1]) # |1⟩
6
# Create 2-qubit states using tensor product
state_00 = np.kron(state_0, state_0) # |00⟩
state_01 = np.kron(state_0, state_1) # |01⟩
state_10 = np.kron(state_1, state_0) # |10⟩
state_11 = np.kron(state_1, state_1) # |11⟩
# Print the 2-qubit states
print("State |00⟩:", state_00)
# print("State |01⟩:", state_01)
# print("State |10⟩:", state_10)
# print("State |11⟩:", state_11)
# Create the equal superposition
equal_superposition = (1/np.sqrt(2)) *(state_00 + state_01 + state_10 + state_11)
# Create a 4x4 identity matrix
I = np.eye(4)
# Create CNOT, CZ, SWAP
out_0000= np.outer(state_00, state_00)
out_0101= np.outer(state_01, state_01)
out_1010= np.outer(state_10, state_10)
out_1111= np.outer(state_11, state_11)
out_1011= np.outer(state_10, state_11)
out_1110= np.outer(state_11, state_10)
out_1001= np.outer(state_10, state_01)
out_0110= np.outer(state_01, state_10)
#print("outer product 0000: \n", out_0000)
#print("outer product 0101: \n", out_0101)
#print("outer product 1010: \n", out_1010)
#print("outer product 1111: \n", out_1111)
#print("outer product 1011: \n", out_1011)
#print("outer product 1110: \n", out_1110)
#print("outer product 1001: \n", out_1001)
#print("outer product 0110: \n", out_0110)
CNOT = out_0000 + out_0101 + out_1011 + out_1110
#print("CNOT: \n", CNOT)
7
CZ = out_0000 + out_0101 + out_1010 - out_1111
#print("CZ: \n", CZ)
SWAP = out_0000 + out_1001 + out_0110 + out_1111
#print("SWAP: \n", SWAP)
# Apply the Identity Gate to the superposition state
new_state = np.dot(I, equal_superposition)
#print("Identity Gate:")
#print(new_state)