import numpy as np
from scipy.stats import trapezoid
from sympy import integrate
from scipy.integrate import quad
from sympy import *
import numpy as np
from sympy import symbols

A = 0.1
B = 1.3
n = 1000
h = (B - A) / n

x, y = symbols('x y')
#Defining the integral
def f(x):
    return 5 * x * np.exp(-2 * x)
#My way
def integral(A, B, n):
    h = (B - A) / n
    y = (1 / 2) * f(A) + (1 / 2) * f(B)
    for i in range(1, n):
        y += f(A + i * h)
    y *= h
    return y
print("Integration my way", integral(A, B, n))
#Professor way
def integral2(A,B, n):
    h = ( B- A)/n
    total_sum = (1 / 2) * (f(A) + f(B))
    for i in range (1, n-1):
        total_sum += f(A + i * h)
    return h * total_sum
print("Integration Prof Way", integral2(A,B,n))
# Calculate the integral
integral_value = integral(A, B, n)
print(f"The integral value is: {integral_value}")
def integrand(x):
    return (5 * x * np.exp(-2 * x))
result = quad(integrand, 0.1, 1.3)
print(result)
#Trapeoidal Way using scipy.integrate
x_val = np.linspace(A, B, n)
y_val = f(x_val)
result_trapz = np.trapezoid(y_val,x_val)
print("Trapezoidal Integration",result_trapz)
####################################################

#Part 2
A2 = 0
B2 = np.pi
n2 = 1000
h2 = (B2 - A2) / n2

x, y = symbols('x y')
#Defining the integral
def f2(x):
    return x ** 2 * np.sin(x) #dx
#My way
def integral(A2, B2, n2):
    h2 = (B2 - A2) / n2
    y = (1 / 2) * f(A) + (1 / 2) * f(B)
    for i in range(1, n):
        y += f(A2 + i * h2)
    y *= h2
    return y
print("\n New bounds and question 2 ", integral(A2, B2, n2))
#Trapeoidal Way using scipy.integrate
x_val2 = np.linspace(A2, B2, n2)
y_val2 = f(x_val2)
result_trapz2 = np.trapezoid(y_val2,x_val2)
print("Trapezoidal Integration",result_trapz2)
####################################################
#Number 3
#Part 2
A3 = 0.5
B3 = 2.3
n3 = 1000
h3 = (B3 - A3) / n3

x, y = symbols('x y')
#Defining the integral
def f3(x):
    return 5* ((np.sin(8 * x)) ** 2)  * np.exp(-1 * (x ** 2)) -13 * np.cos(3 * x) #dx
#My way
def integral(A3, B3, n3):
    h3 = (B3 - A3) / n3
    y = (1 / 2) * f(A) + (1 / 2) * f(B)
    for i in range(1, n):
        y += f(A3 + i * h3)
    y *= h3
    return y
print("\n New bounds and question 3", integral(A3, B3, n3))
#Trapeoidal Way using scipy.integrate
x_val3 = np.linspace(A3, B3, n3)
y_val3 = f(x_val3)
result_trapz3 = np.trapezoid(y_val3,x_val3)
print("Trapezoidal Integration",result_trapz3)
####################################################
#Number 4
A4 = -5
B4 = 5
n4 = 1000

# Define the function for the upper half of the circle
def f4(x):
    return np.sqrt(25 - (x ** 2))


# Trapezoidal integration function
def trapezoidal_integration(f4, A4, B4, n4):
    h4 = (B4 - A4) / n4
    result4 = (1 / 2) * f4(A4) + (1 / 2) * f4(B4)
    for i in range(1, n4):
        result4 += f4(A4 + i * h4)
    result4 *= h4
    return result4
#second way
x_val4 = np.linspace(A4, B4, n4)
y_val4 = f4(x_val4)

#2 ways
result_trapz4 = trapezoidal_integration(f4, A4, B4, n4)
result_trapz4z = np.trapezoid(y_val4,x_val4) # Trapezoidal Way

# Because there is an upper and lower bounds in the circle but it's the same, we just double it
area = 2 * result_trapz4 # or trapz4z
print("Trapezoidal Integration for the circle problem:", area)