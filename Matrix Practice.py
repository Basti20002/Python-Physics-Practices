import numpy as np
from numpy import *
from numpy.linalg import *
from sympy.codegen import Print

##how to create a Matrix
#Matrix1 = np.array(([#,#],[#,#]))
##* is easily enough just multiplying the one values together, but there needs to be the prior import first
## dot does the correct multiplication of the matrixes
M1 = np.array(([0,1],[1,3]))
print(M1)
M2 = np.array(([-1,3],[5,2]))
print(M2)
Addition_M = M1 + M2
print(Addition_M)
Subtraction_M = M1 - M2
#this is the weird one
print(Subtraction_M)
print(M1*M2)
#this is the correct one
dot_M = np.dot(M1,M2)
print(dot_M)
#creating a matrix using reshape?
A1 = np.arange(12)
#creates a 12x1 matrix
print(A1)
A2 = np.arange(12).reshape((3,4))
#creates a 3x4 matrix with the reshape
print(A2)
#shape explains what you did with the reshape
print(A2.shape)
#ndim tells you what kind of arange you created
#ndim 0-> is one value, 1 -> vector (Seqeunce)
#ndim 2 -> matrix, 3 -> cube
print(A1.ndim)
print(A2.ndim)
print(A2.size)


#Off to transpose, FLIPS ROW AND COLUMN
A2_Transpose1 = A2.T
print (A2_Transpose1)
#another way
A2_Transpose2 = np.transpose(A2)
print(A2_Transpose2)

#Calculating the determinant
det_M2 = np.linalg.det(M2)
print("Determinant of M2", det_M2)
det_M1 = np.linalg.det(M1)

#class practice to do exponentials
#the first two values
k = 1
x = .1
d1 = np.e**-(1j*k*x)
d2 = np.e**(1j*k*x)
M3 = np.array(([0,d1],[d2,0]))
print(M3)



#Calculating the inverse
B1 = np.array(([3,3,-2],[2,5,0],[3,1,2]))
print(B1)
det_B1 = np.linalg.det(B1)
print("determinant of the matrix B",det_B1)
N_inverse = np.linalg.inv(B1)
det_InvB1 = np.linalg.det(N_inverse)
print(det_InvB1)
print("inverse of the B1", N_inverse)
dot_B1 = np.dot(B1,N_inverse)
print(dot_B1)

#Define for prompt 3
Sx = np.array(([0,1],[1,0]))
Sy = np.array(([0, -1j],[1j,0]))
Sz = np.array(([1,0],[0,-1]))
#2
Sx_dot = np.dot(Sx,Sx)
Sy_dot = np.dot(Sy,Sy)
Sz_dot = np.dot(Sz,Sz)
print(Sx_dot)
print(Sy_dot)
print(Sz_dot)
#3
Sx_Herm = Sx.conj().T
print("Hermitian of Sx",Sx_Herm)
#4
Four = np.dot(Sx_Herm, Sx)
print(Four)
#5
Five = np.trace(Sx)
print(Five)


