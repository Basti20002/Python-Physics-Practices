import numpy as np
import matplotlib.pyplot as plt

#Root will have to be between lower and upper bounds, a,b so make sure if you
#Dont get anything in the plot or value, that is the reason.

#Precision, Interval [a,b] and maximum iterations
eps = 1e-3 #Precision
Nmax = 100 #iterations
a = 0
b = 8
#Define the function
def f(x):
    return 2 * np.cos(x) - x

#Bisection algorithm
def Bisection(Xminus, Xplus, Nmax, eps):
    # Check if the initial interval is valid
    if f(Xminus) * f(Xplus) >= 0:
        print("Bisection method fails: f(Xminus) and f(Xplus) must have opposite signs.")
        return None
    print(f"Starting Bisection Method on [{Xminus}, {Xplus}] with eps = {eps}")

    for it in range(Nmax): # it = iteration counter, it starts from 0 to Nmax - 1
        x = (Xplus + Xminus) / 2 #Midpoint
        fx = f(x)
        print(f"Iteration {it}: x = {x}, fx = {fx}")
        #Narrow the Intervals
        if f(Xplus) * fx > 0:
            Xplus = x
        else:
            Xminus = x
        #Checking for convergence
        if abs(fx) < eps:
            print(f"\n Root found with precision eps = {eps} after {it +1} iterations")
            return x
    print("\n No root found after maximum iterations.")
    return None
#Call the bisection Method
root = Bisection(a, b, Nmax, eps)
if root is not None:
    print(f"Root = {root}")
#Plotting the function and roots
x_vals = np.linspace(a,b, 500)
y_vals = f(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label=r"$f(x) = 2\cos(x) - x$", color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
if root is not None:
    plt.scatter(root, f(root), color='red', label=f"Root ≈ {root:.4f}") # scatter function to display a point,
# f-string formatting to create a dynamic string. {root:.4f} formats the value of root to 4 decimal places.
plt.title("Bisection Method: Finding the Root of $f(x)$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()



#Second way Newton-Raphson Method
from math import cos
x0 = 1111 # initial guess
dx = 3.e-4 # Step Size
eps = 0.002 # Tolerance
Nmax = 100 # Max Iterations
def f(x):
    return 2 * cos(x) - x
def NewtonR(x, dx, eps, Nmax):
    for it in range(Nmax):
        F = f(x)
        if abs(F) <= eps:
            print(f'\nRoot found: f(root) = {F}, eps = {eps}')
            break
        print(f'Iteration # = {it + 1}, x = {x}, f(x) = {F}') # it starts from 0 so Iteration = it + 1
# Central difference approximation for the derivative
        df = (f(x + dx / 2) - f(x - dx / 2)) / dx # dx = h is step size
# Update the value of x using the Newton-Raphson formula
        dx_new = -F / df # xnew = xold - f/f'
        x += dx_new
    else: # This part runs if the loop doesn't break
        print(f'\nNewton failed for Nmax = {Nmax}')
    return x
root = NewtonR(x0, dx, eps, Nmax)
print("Root found:", root)


#F solve way

import numpy as np
from scipy.optimize import fsolve
#Define the function for root finding Im just going to use the same function here.
def g(x):
    return 2 * np.cos(x) - x
#initial guess,
x_guess = 3
#solve for the x value
x_solution = fsolve(g, x_guess)

#print this solution out. the .#f gives you the solution with # of significant figures.
#in this case, the answer will be 1.03 instead of a crazy thread. this can be changed with .5f
print(f"x: {x_solution[0]: .2f}")
















#Last ways is via Newton-Raphson algorithm/ Technically this is already written but I rewrote this for practice
from math import cos
xo = 1111 # Initial guess
dx = 3.e-4 # 3x10^(-4) per step
eps = 0.002 # Tolerance
Nmax = 100 # Max iterations

def h(x):
    return 2 * cos(x) - x
def NewtonR(x, dx, eps, Nmax):
    for it in range(Nmax):
        F = h(x)
        if abs(F) <= eps:
            print(f'\nRoot found: f(root) = {F}, eps = {eps}')
            break
        print(f'Iteration # = {it + 1}, x = {x}, h(x) = {F}') # it starts from 0 so iteration = it + 1

        # Central difference approximation for the derivative
        df = (f(x+ dx / 2) - f(x -dx / 2)) / dx #dx = h step size

        #Update the value of x using the Newton-Raphson formula
        dx_new = -F / df    #Xnew = xold - f/f'
        x += dx_new
    else: #This part runs if the loop doesn't break
        print(f'\nNewton failed for Nmax = {Nmax}')

    return x
print("\n Newton Method Answer")
root = NewtonR(xo, dx, eps, Nmax)
print("Root found:", root)
