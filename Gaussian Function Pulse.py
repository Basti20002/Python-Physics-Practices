import numpy as np
import matplotlib.pyplot as plt

# Defining parameters
A = 1.0
#mu moves it from left to right,
mu = 2.5  # Center the Gaussian at L/2
sigma = 0.1
L = 5
Nx = 500
dx = L / (Nx-1)

# Function
#def gaussian(x, A, mu, sigma):
    #return A * np.exp(-((x - mu)**2) / (2 * sigma**2))

# Generate x values
x = np.linspace(0, L, Nx)

# Compute y values using the Gaussian function
#y = gaussian(x, A, mu, sigma)

#Another way is to just put in the function and call it a day
y = A * np.exp(-((x - mu)**2) / (2 * sigma**2))
# Plot the Gaussian function
plt.plot(x, y)
plt.title('Gaussian Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
