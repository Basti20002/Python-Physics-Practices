import math
import numpy as np
import scipy.integrate as spi
from scipy.integrate import quad

#Define function
def f(x):
    return 5 * (np.sin(8 * x)) ** 2 * np.exp(-1 **2) - 13 * np.cos(3 * x)

#Integration limits, a being upper and b being lower
a = 0.5
b = 2.3

#Style 1 using quad which means adaptive Quadrature.
result_quad, error = quad(f, a, b)
print(f"quad: {result_quad}, Error: {error}")

#Style 2 using trapezoidal rule
x_vals = np.linspace(a ,b, 1000)
y_val = f(x_vals)
result_trapz = np.trapezoid(y_val, x_vals)
print(f"Trapezoidal Method: {result_trapz}")

#3 Using Simpsons Rule
result_simps = spi.simpson(y_val,x_vals)
print(f"Simpson's Rule: {result_simps}")

print("\n:")

#Number 2


a2 = 0
b2 = np.pi
n2 = 1000
h2 = (b2 - a2) / n2
#Defining the integral
def f2(x):
    return x ** 2 * np.sin(x) #dx
#Style 1 using quad which means adaptive Quadrature.
result_quad2, error = quad(f2, a2, b2)
print(f"quad: {result_quad2}, Error: {error}")

#Style 2 using trapezoidal rule
x2_vals = np.linspace(a2 ,b2, 1000)
y2_val = f2(x2_vals)
result_trapz2 = np.trapezoid(y2_val, x2_vals)

print(f"Trapezoidal Method: {result_trapz2}")

#3 Using Simpsons Rule
result_simps2 = spi.simpson(y2_val,x2_vals)
print(f"Simpson's Rule: {result_simps2}")


#Number 1
print("\n:")

a3 = 0.1
b3 = 1.3
n3 = 1000
#Defining the integral
def f3(x):
    return (5 * x * np.exp(-2 * x))
#Style 1 using quad which means adaptive Quadrature.
result_quad3, error = quad(f3, a3, b3)
print(f"quad: {result_quad3}, Error: {error}")

#Style 2 using trapezoidal rule
x3_vals = np.linspace(a3 ,b3, 1000)
y3_val = f3(x3_vals)
result_trapz3 = np.trapezoid(y3_val, x3_vals)

print(f"Trapezoidal Method: {result_trapz3}")

#3 Using Simpsons Rule
result_simps3 = spi.simpson(y3_val,x3_vals)
print(f"Simpson's Rule: {result_simps3}")


#My own integral problem
print("\n:")
a4 = 0.5
b4 = 2.3
n4 = 500

#defining the integral
def f4(x):
    return 5 * (np.sin(8 * x)) ** 2 * np.exp((-1*x) ** 2) - 13j * np.cos(3 * x)
#real parts
result_quad4_real, error4 = quad(lambda x: np.real(f4(x)), a4, b4)
print(f"Real Part of the Integral: {result_quad4_real}, Error: {error4}")
#imaginary parts
result_quad4_imag, error4 = quad(lambda x: np.imag(f4(x)), a4, b4)
print(f"Imaginary Part of the Integral: {result_quad4_imag}, Error: {error4}")


#Style 2 using trapezoidal rule
x4_vals = np.linspace(a4 ,b4, 1000)
y4_val = f4(x4_vals)
#real parts
result_trapz4_real = np.trapezoid(np.real(y4_val), x4_vals)
print(f"Trapezoidal Method Real Value: {result_trapz4_real}")
#imaginary parts
result_trapz4_imag = np.trapezoid(np.imag(y4_val), x4_vals)
print(f"Trapezoidal Method imag Value: {result_trapz4_imag}")

result_trapz4 = np.trapezoid(y4_val, x4_vals)
print("\n:")
print(f"Trapezoidal Method: {result_trapz4}")
print("\n:")
#3 Using Simpsons Rule
result_simps4 = spi.simpson(y4_val,x4_vals)
print(f"Simpson's Rule: {result_simps4}")