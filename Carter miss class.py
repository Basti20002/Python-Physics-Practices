from token import N_TOKENS

import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.bezier import inside_circle
from math
from numpy import *
from prompt_toolkit import pep440


def estimate_pi(N_samples):
    inside_circle = 0
    for _ in range(N_samples):
        #This generates random points between [-1,1]
        x,y = random.uniform(-1,1), random.uniform(-1,1)

        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
#The ration of points inside the circle to total points approxiamtes pi/4
    return 4 * inside_circle / N_samples
#Run the simulation using 1,000,000 samples
N_samples =1000000
estimated_pi = estimate_pi(N_samples)

print(f"Estimated Value of pi: {estimated_pi}")
#For plotting
x = np.random.rand(N_samples)
y = np.random.rand(N_samples)
D = x ** 2 + y ** 2
inside_circle = D <= 1
#Plots
plt.gca().add_patch(plt.Rectangle((0,0), 1, 1, color='#0000FA', alpha= 0))

theta = np.linspace(0, np.pi / 2, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)
plt.plot(x_circle,y_circle, color='black', lw= 1)
#plt.fill(x_circle,y_circle, color='orange', alpha=0, lw= 1)

#plot the points
plt.scatter(x, y, color='#0000FA', s=1) #All points
plt.scatter(x[inside_circle], y[inside_circle], color='#B2F1A5', s=1)
#Labels
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Monte Carlo Simulation: Square and Quadrant')
#plot limits
plt.xlim(0,1)
plt.ylim(0,1)
plt.gca().set_aspect('equal', adjustable='box')
#plot legend
plt.legend()
#plot show
#plt.show()






#New Section
N, Npts= 100, 5000
analyt=np.pi**2
x1 = np.arange(0,2*np.pi + 2*np.pi/N, 2*np.pi/N)
xi=[]; yi=[]; xo=[]; yo=[]

fig,ax = plt.subplots()
y1 = x1*np.sin(x1)**2
ax.plot(x1, y1, 'c', linewidth=4)
ax.set_xlim(0,2*np.pi)
ax.set_ylim(0,5)
ax.set_xticks([0,np.pi,2*np.pi])
ax.set_xticklabels(['0', '$\pi$', '2$\pi$'])
ax.set_xlabel('x', fontsize=20)
ax.set_ylabel('$f(x)=x\, \sin^2 x$', fontsize=20)
#fig.patch.set_visible(False)

def fx(x):
    return x*np.sin(x) ** 2
xx = 2 * np.pi*np.random.rand(Npts)
yy = 5 * np.random.rand(Npts)

boxarea = 2 * np.pi * 5
j = 0
for i in range(1, Npts):
    if (yy[i] <= fx(xx[i])):
        xi.append(xx[i])
        yi.append(yy[i])
        j += 1
    else:
        yo.append(yy[i])
        xo.append(xx[i])

    area = boxarea*j/(Npts-1)
ax.plot(xo,yo,'bo', markersize=1)
ax.plot(xi, yi, 'ro', markersize=1)
ax.set_title('Answers: Analytic = %5.3f, MC=%5.3f' %(analyt,area))

plt.show()




#Trapezoidal Rule

#define the function to integrate
def F(x):
    return 5*(np.sin(8 * x)) ** 2 * np.exp(-x * x) -13 * np.cos(3 * x)
#Trap rule implementation
def trap(A,B,n):
    h = (B-A)/n
    tot_sum = (F(A)+F(B)) / 2
    for i in range (1, N-1):
        tot_sum += F(A + i * h)
    return h * tot_sum
#set integration limits and number of steps
A = 0.5
B = 2.3
n = 1200
#Print the results of the integration
#print(trap(A, B, n))
print(f"The estimated integral is: {trap(A, B, n)}")





#Gauss-Legendre Quadrature

#Defining the function to compute these with nodes
def GaussP(Npts, a, b, x, w, eps):
    m = int((Npts + 1) / 2) #Number of nodes to compute (half of Npts rounded up)

    for i in range(1, m + 1):
        #initial approx of the root using the cosine function
        t = math.cos(math.pi * (float(i) -0.25) / (float(Npts)+ 0.5))
        t1 =1

        while abs(t-t1) >= eps: #iterating to the code to improve the root estimate
            p1 = 1
            p2 = 0
            # Recursively calculate the Legendre polynomial P_n(t)
            for j in range(1, Npts +1):
                p3 = p2
                p2 = p1
                p1 = ((2 * float(j) -1) * t * p2 - (float(j) -1) p3) / float(j)

            #Calculating the derivative of the polynomial
            pp = Npts * (t* p1 -p2) / (t * t -1)
            t1 = t
            t = t1 - p1 / pp
        #Store the nodes and weights
        x[i-1] = -t # The roots of the legendre polynomial
        x[Npts - i] = t
        w[i - 1] = 2 / ((1 - t * t)* pp * pp) #Weights
        w[Npts - i] = w[i -1]
    #transform the nodes and weights to the interval [a,b]
    for j in range(Npts):
        x[j] = 0.5 * (b-a) * x[j] + 0.5 * (b+a) #Scaling to the interval [a,b]
        w[j] = 0.5 * (b-a) * w[ ]

