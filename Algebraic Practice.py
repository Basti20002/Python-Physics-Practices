import sympy as sp
from sympy import *
x,y = symbols('x y') # Define 'x' as a symbol
# to tell SymPy that x and y should be treated as algebraic symbols
# rather than numerical values.
#1. Compute the derivative of tan(x) with respect to x
y_diff1 = diff(tan(x), x)
#print("derivative of tan(x): \n", y_diff1)

#2. 1st order derivative
y_diff2=diff(5*x**4 + 7*x**2, x, 1) #dy/dx
print("1st order derivative of 5x^4 + 7x^2: \n", y_diff2)
#3. 2nd order derivative
y_diff3=diff(5*x**4 + 7*x**2, x, 2) #d^2y/dx^2
#print("2nd order derivative of 5x^4 + 7x^2: \n", y_diff3)
#4. expansion
z = (x + y)**8
print("expression of z: \n",z)
print("expansion of z: \n",expand(z))
#5. series
series_1 = sin(x).series(x,0) # Maclaurin series of sin(x) (Taylor)
#print("series 1: \n",series_1)
series_2 = sin(x).series(x,10) # Taylor series of sin(x)
#print("series 2: \n",series_2)
series_3 = 1/cos(x)
#print("series 3: \n",series_3)
series_4 = series_3.series(x,0) # Taylor series of 1/cos(x)
print("series 4: \n", series_4)
#6. factor and simplify
f1 = factor(x**2 - 1) # (x-1)(x+1)
f2 = factor(x**3 - x**2 + x - 1) # (x - 1)*(x**2 + 1)
f3 = simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x +1)) # (x-1)
f4 = factor(x**3 + 3*x**2*y + 3*x*y**2 + y**3) # (x + y)^3
f5 = simplify(1 + tan(x)**2) # (cosx)^-2
#print("f1: \n",f1)
#print("f2: \n",f2)
#print("f3: \n",f3)
#print("f4: \n",f4)
#print("f5: \n",f5)
#7. Solve a system of equations
eq1 = sp.Eq(x**2 + y**2, 25) # x^2 + y^2 = 25 (Equation of a circle)
eq2 = sp.Eq(x - y, 3) # x - y = 3
solutions = sp.solve((eq1, eq2), (x, y))
print("solution: \n", solutions)