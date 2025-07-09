import sys, time
import math as m
import numpy as np
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU

def display():
	# Clear off-screen buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	# -- Draw something here
	# -- Pushes off-screen buffer to the videoram
    glutSwapBuffers()

# Initialize Glut
glutInit()
# Create a double-buffer RGBA window.   (Single-buffering is possible. So is creating an index-mode window.)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

# Create a window, setting its title
glutCreateWindow('interactive')
glutInitWindowSize(1200, 600)

# Set the display callback.  You can set other callbacks for keyboard and mouse events.
glutDisplayFunc(display)

def idle():
	while True:
		time.sleep(0.1)

glutIdleFunc(idle)

# Run the GLUT main loop until the user closes the window.
glutMainLoop()
