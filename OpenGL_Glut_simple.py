import sys, time
import math
import numpy

import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *

def idle():
	while True:
		time.sleep(0.1)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b'linkage')

# initWindow()

glutIdleFunc(idle)
glutMainLoop()