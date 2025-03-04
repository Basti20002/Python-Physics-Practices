from scipy.integrate import quad
import numpy as np

# Define the function to integrate
def integrand(x):
    return 5 * x * np.exp(-2 * x)

# Compute the definite integral from 0.1 to 1.3
result, error = quad(integrand, 0.1, 1.3)

print(f"Definite integral of 5x(e^(-2x)) from 0.1 to 1.3 is: {result}")

import numpy as np

# Define the function for the upper half of the circle
def f(x):
    return np.sqrt(25 - x**2)

# Trapezoidal integration function
def trapezoidal_integration(f, a, b, n):
    h = (b - a) / n
    result = (1 / 2) * f(a) + (1 / 2) * f(b)
    for j in range(1, n):
        result += f(a + j * h)
    result *= h
    return result

# Parameters
a = -5  # Lower bound of integration
b = 5   # Upper bound of integration
n = 1000  # Number of trapezoids

# Calculate the integral for the upper half of the circle
integral_value = trapezoidal_integration(f, a, b, n)

# Multiply by 2 to account for the lower half of the circle
area = 2 * integral_value

print(f"The area of the circle with radius 5 m is approximately: {area} square meters")