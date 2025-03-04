from vpython import * # Correct library
import numpy as np # For using arange (or np.linspace)
posy = 100 # position y
Lcord = 250 # length of cord
Height = 50 # height of cylinder
# Initial parameters
scene = canvas(height=600, width=600, range=380) # 600 pixels
# Creating the ground and division lines
alt = curve(pos=[(-300, posy, 0), (300, posy, 0)]) # two endpoints of the curve, altitude
divi = curve(pos=[(0, -150, 0), (0, posy, 0)]) # division
# Creating the mass (red cylinder) and cords (yellow cylinders)
kilogr = cylinder(pos=vector(0, 50, 0), radius=20, axis=vector(0, -200, 0),
color=color.blue)