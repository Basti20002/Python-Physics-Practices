from vpython import * # Correct library
import numpy as np # For using arange (or np.linspace)
# Initial parameters
posy = 100 # position y
Lcord = 250 # length of cord
Height = 50 # height of cylinder
W = 10
v = 2
x1 = 0
# Create the display scene
scene = canvas(height=600, width=600, range=380) # 600 pixels
# Creating the ground and division lines
alt = curve(pos=[(-300, posy, 0), (300, posy, 0)]) # two endpoints of the curve, altitude
divi = curve(pos=[(0, -150, 0), (0, posy, 0)]) # division
# Creating the mass (red cylinder) and cords (yellow cylinders)
kilogr = cylinder(pos=vector(0, posy - Lcord, 0), radius=20, axis=vector(0, -Height, 0),
color=color.red)
cord1 = cylinder(pos=vector(0, posy, 0), axis=vector(0, -Lcord, 0), color=color.yellow,
radius=2)
cord2 = cylinder(pos=vector(0, posy, 0), axis=vector(0, -Lcord, 0), color=color.yellow,
radius=2)
# Creating the force arrows
arrow1 = arrow(pos=vector(0, posy, 0), color=color.cyan)
arrow2 = arrow(pos=vector(0, posy, 0), color=color.cyan)
# Labels for angle and force
anglabel = label(pos=vector(0, 240, 0), text='angle (deg)', box=0)
#box = 0 disables the box around the label
angtext = label(pos=vector(20, 210, 0), box=0)
Flabel1 = label(pos=vector(200, 240, 0), text='Force', box=0)
Ftext1 = label(pos=vector(200, 210, 0), box=0)
Flabel2 = label(pos=vector(-200, 240, 0), text='Force', box=0)
Ftext2 = label(pos=vector(-200, 210, 0), box=0)
# Adding light to the scene
local_light(pos=vector(-10, 0, 20), color=color.red)
# Animation loop
for t in np.arange(0, 100, 0.2): # Use np.arange instead of arange
    rate(50) # speed of animation, <50 iterations per second
    x1 = v * t # Horizontal displacement of the object (cord end, not cylinder)
    theta = np.arcsin(x1 / Lcord) # Using np.arcsin for angle calculation
# Update the vertical position of the mass based on the angle
    poscil = posy - Lcord * np.cos(theta)
    kilogr.pos = vector(0, poscil, 0)
# Calculate force (F = W / cos(theta)) and update the angle
    magF = W / (2 * np.cos(theta)) # Force calculation
    angle = 180 * theta / np.pi # Convert angle to degrees
# Update the positions and directions of the cords
    cord1.pos = vector(x1, posy, 0)
    cord1.axis = vector(-Lcord * np.sin(theta), -Lcord * np.cos(theta), 0)
    cord2.pos = vector(-x1, posy, 0)
    cord2.axis = vector(Lcord * np.sin(theta), -Lcord * np.cos(theta), 0)
# Update the force arrows
    arrow1.pos = cord1.pos
    arrow1.axis = vector(8 * magF * np.sin(theta), 8 * magF * np.cos(theta), 0)
    arrow2.pos = cord2.pos
    arrow2.axis = vector(-8 * magF * np.sin(theta), 8 * magF * np.cos(theta), 0)
# Update labels with current angle and force
    angtext.text = f'{angle:.2f}' # Display angle in degrees
    force = magF
    Ftext1.text = f'{force:8.2f}' # Force on the first cord
    Ftext2.text = f'{force:8.2f}' # Force on the second cord
# Keep the window open
while True:
    rate(60) # Keeps the scene running (or pass)