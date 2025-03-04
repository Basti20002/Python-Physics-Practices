import numpy as np
x = [0,1,2,3,4,5,6,7,8,9]
xo = np.zeros_like(x)
x1 = np.hstack([x,xo])
x2 = np.zeros(len(x))
print(x)
print(xo)
print(x1)
print(x2)
