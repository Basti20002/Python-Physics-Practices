import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
from scipy.integrate import quad
import math

# Define the integrand functions
def integrand_I12(x):
    return 2 * np.sin(x) * np.exp(-3j * x) + 3 * np.cos(x) * np.exp(-1j * x)

def integrand_I44(x):
    return np.conj(integrand_I12(x))

# Monte Carlo integration function
def monte_carlo_integration(func, a, b, num_samples):
    samples = np.random.uniform(a, b, num_samples)
    func_values = func(samples)
    integral = (b - a) * np.mean(func_values)
    return integral, samples, func_values

# Define the integration limits and number of samples
a = 0
b = np.pi / 5
num_samples = 25000

# Perform the Monte Carlo integration for I12 and I44
I12_mc, samples_I12, func_values_I12 = monte_carlo_integration(integrand_I12, a, b, num_samples)
I44_mc, samples_I44, func_values_I44 = monte_carlo_integration(integrand_I44, a, b, num_samples)

# Integration using adaptive quadrature (quad)
I12_quad, error_I12_quad = quad(lambda x: integrand_I12(x).real, a, b)
I12_quad += 1j * quad(lambda x: integrand_I12(x).imag, a, b)[0]

I44_quad, error_I44_quad = quad(lambda x: integrand_I44(x).real, a, b)
I44_quad += 1j * quad(lambda x: integrand_I44(x).imag, a, b)[0]

# Integration using the trapezoidal rule
x_vals = np.linspace(a, b, num_samples)
y_vals_I12 = integrand_I12(x_vals)
y_vals_I44 = integrand_I44(x_vals)

I12_trapz = np.trapz(y_vals_I12, x_vals)
I44_trapz = np.trapz(y_vals_I44, x_vals)

# Integration using Simpson's rule
I12_simps = spi.simpson(y_vals_I12, x_vals)
I44_simps = spi.simpson(y_vals_I44, x_vals)



# Create the 4x4 matrix and assign the computed integrals
matrix_mc = np.zeros((4, 4), dtype=complex)
matrix_mc[0, 1] = I12_mc
matrix_mc[3, 3] = I44_mc

matrix_mc2 = np.array([
    [0, I12_mc, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, I44_mc]
], dtype=complex)

matrix_quad = np.zeros((4, 4), dtype=complex)
matrix_quad[0, 1] = I12_quad
matrix_quad[3, 3] = I44_quad

matrix_quad2 = np.array([
    [0, I12_quad, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, I44_quad]
], dtype=complex)

matrix_trapz = np.zeros((4, 4), dtype=complex)
matrix_trapz[0, 1] = I12_trapz
matrix_trapz[3, 3] = I44_trapz

matrix_trapz2 = np.array([
    [0, I12_trapz, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, I44_trapz]
], dtype=complex)

matrix_simps = np.zeros((4, 4), dtype=complex)
matrix_simps[0, 1] = I12_simps
matrix_simps[3, 3] = I44_simps

matrix_simps2 = np.array([
    [0, I12_simps, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, I44_simps]
], dtype=complex)


# Print the results
print("Monte Carlo Integration Matrix Zero:")
print(matrix_mc)
print("Monte Carlo Integration Matrix Array:")
print(matrix_mc2)
print(f"I12 (Monte Carlo): {I12_mc}")
print(f"I44 (Monte Carlo): {I44_mc}")

print("\nAdaptive Quadrature Integration Matrix Zero:")
print(matrix_quad)
print("\nAdaptive Quadrature Integration Matrix Array:")
print(matrix_quad2)
print(f"I12 (quad): {I12_quad}, Error: {error_I12_quad}")
print(f"I44 (quad): {I44_quad}, Error: {error_I44_quad}")

print("\nTrapezoidal Rule Integration Matrix Zero:")
print(matrix_trapz)
print("\nTrapezoidal Rule Integration Matrix Array:")
print(matrix_trapz2)
print(f"I12 (trapezoidal): {I12_trapz}")
print(f"I44 (trapezoidal): {I44_trapz}")

print("\nSimpson's Rule Integration Matrix Zero:")
print(matrix_simps)
print("\nSimpson's Rule Integration Matrix Array:")
print(matrix_simps2)
print(f"I12 (Simpson's): {I12_simps}")
print(f"I44 (Simpson's): {I44_simps}")


# Define the function to compute the Gauss-Legendre nodes and weights just for fun
def GaussPoints(Npts, a, b, eps=1e-14):
    x = np.zeros(Npts)
    w = np.zeros(Npts)
    m = int((Npts + 1) / 2)  # Number of nodes to compute (half of Npts rounded up)
    for i in range(1, m + 1):
        t = math.cos(math.pi * (float(i) - 0.25) / (float(Npts) + 0.5))
        t1 = 1
        while abs(t - t1) >= eps:
            p1 = 1
            p2 = 0
            for j in range(1, Npts + 1):
                p3 = p2
                p2 = p1
                p1 = ((2 * float(j) - 1) * t * p2 - (float(j) - 1) * p3) / float(j)
            pp = Npts * (t * p1 - p2) / (t * t - 1)
            t1 = t
            t = t1 - p1 / pp
        x[i - 1] = -t
        x[Npts - i] = t
        w[i - 1] = 2 / ((1 - t * t) * pp * pp)
        w[Npts - i] = w[i - 1]
    for j in range(Npts):
        x[j] = 0.5 * (b - a) * x[j] + 0.5 * (b + a)
        w[j] = 0.5 * (b - a) * w[j]
    return x, w

# Define the integration limits and number of points
Npts = 100
# Compute the Gauss-Legendre nodes and weights
x, w = GaussPoints(Npts, a, b)
# Perform the integration for I12 and I44
I12_leg = np.sum(w * integrand_I12(x))
I44_leg = np.sum(w * integrand_I44(x))
# Create the 4x4 matrix and assign the computed integrals
matrix_leg = np.zeros((4, 4), dtype=complex)
matrix_leg[0, 1] = I12_leg
matrix_leg[3, 3] = I44_leg

# Print the results
print("Matrix Gauss Legendre:")
print(matrix_leg)
print(f"I12: {I12_leg}")
print(f"I44: {I44_leg}")

# Plotting the integration for I12 and I44
x1 = np.linspace(a, b, 1000)
y1 = integrand_I12(x1)
x2 = np.linspace(a, b, 1000)
y2 = integrand_I44(x2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# Plot for I12
ax1.plot(x1, y1.real, 'c', linewidth=4, label='Real part of integrand')
ax1.plot(x1, y1.imag, 'm', linewidth=4, label='Imaginary part of integrand')
ax1.set_xlim((a, b))
ax1.set_ylim((min(0, y1.imag.min()), max(y1.real.max(), y1.imag.max())))
ax1.set_xticks([0, np.pi / 10, np.pi / 5])
ax1.set_xticklabels(['0', '$\pi/10$', '$\pi/5$'])
ax1.set_xlabel('x', fontsize=20)
ax1.set_ylabel('Integrand', fontsize=20)

# Monte Carlo points for I12
xi = np.random.uniform(a, b, num_samples)
yi_real = np.random.uniform(0, max(y1.real.max(), y1.imag.max()), num_samples)
yi_imag = np.random.uniform(min(0, y1.imag.min()), max(y1.imag.max(), y1.imag.max()), num_samples)

# Separate points inside and outside the function for real part
inside_real_x = []
inside_real_y = []
outside_real_x = []
outside_real_y = []

for i in range(num_samples):
    if yi_real[i] <= integrand_I12(xi[i]).real:
        inside_real_x.append(xi[i])
        inside_real_y.append(yi_real[i])
    else:
        outside_real_x.append(xi[i])
        outside_real_y.append(yi_real[i])

# Separate points inside and outside the function for imaginary part
inside_imag_x = []
inside_imag_y = []
outside_imag_x = []
outside_imag_y = []

for i in range(num_samples):
    if yi_imag[i] <= integrand_I12(xi[i]).imag:
        inside_imag_x.append(xi[i])
        inside_imag_y.append(yi_imag[i])
    else:
        outside_imag_x.append(xi[i])
        outside_imag_y.append(yi_imag[i])

# Plot Monte Carlo points for I12
ax1.plot(outside_real_x, outside_real_y, 'bo', markersize=1, label='MC Real points outside')
ax1.plot(inside_real_x, inside_real_y, 'ro', markersize=1, label='MC Real points inside')
ax1.plot(outside_imag_x, outside_imag_y, 'go', markersize=1, label='MC Imag points inside')
ax1.plot(inside_imag_x, inside_imag_y, 'yo', markersize=1, label='MC Imag points outside')

ax1.legend()
ax1.set_title('Monte Carlo Integration\n$I_{12}$: Real and Imaginary Parts')

# Plot for I44
ax2.plot(x2, y2.real, 'c', linewidth=4, label='Real part of integrand')
ax2.plot(x2, y2.imag, 'm', linewidth=4, label='Imaginary part of integrand')
ax2.set_xlim((a, b))
ax2.set_ylim((min(0, y2.imag.min()), max(y2.real.max(), y2.imag.max())))
ax2.set_xticks([0, np.pi / 10, np.pi / 5])
ax2.set_xticklabels(['0', '$\pi/10$', '$\pi/5$'])
ax2.set_xlabel('x', fontsize=20)
ax2.set_ylabel('Integrand', fontsize=20)

# Monte Carlo points for I44
xi = np.random.uniform(a, b, num_samples)
yi_real = np.random.uniform(0, max(y2.real.max(), y2.imag.max()), num_samples)
yi_imag = np.random.uniform(min(0, y2.imag.min()), max(y2.imag.max(), y2.imag.max()), num_samples)

# Separate points inside and outside the function for real part
inside_real_x = []
inside_real_y = []
outside_real_x = []
outside_real_y = []

for i in range(num_samples):
    if yi_real[i] <= integrand_I44(xi[i]).real:
        inside_real_x.append(xi[i])
        inside_real_y.append(yi_real[i])
    else:
        outside_real_x.append(xi[i])
        outside_real_y.append(yi_real[i])

# Separate points inside and outside the function for imaginary part
inside_imag_x = []
inside_imag_y = []
outside_imag_x = []
outside_imag_y = []

for i in range(num_samples):
    if yi_imag[i] <= integrand_I44(xi[i]).imag:
        inside_imag_x.append(xi[i])
        inside_imag_y.append(yi_imag[i])
    else:
        outside_imag_x.append(xi[i])
        outside_imag_y.append(yi_imag[i])

# Plot Monte Carlo points for I44
ax2.plot(outside_real_x, outside_real_y, 'bo', markersize=1, label='MC Real points outside')
ax2.plot(inside_real_x, inside_real_y, 'ro', markersize=1, label='MC Real points inside')
ax2.plot(outside_imag_x, outside_imag_y, 'go', markersize=1, label='MC Imag points outside')
ax2.plot(inside_imag_x, inside_imag_y, 'yo', markersize=1, label='MC Imag points inside')

ax2.legend()
ax2.set_title('Monte Carlo Integration\n$I_{44}$: Real and Imaginary Parts')

plt.tight_layout()
plt.show()