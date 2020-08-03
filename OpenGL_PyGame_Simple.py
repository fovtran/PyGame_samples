import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ctypes import *
import numpy as np

pygame.init ()
screen = pygame.display.set_mode ((800,600), pygame.OPENGL|pygame.DOUBLEBUF, 24)
glViewport (0, 0, 800, 600)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_POSITION, (.2, .2, -5))
glEnable(GL_COLOR_MATERIAL)
glClearColor(.3, .1, .3, 1.0)

glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
glEnableClientState (GL_VERTEX_ARRAY)
glLoadIdentity()
glMatrixMode(GL_PROJECTION)
gluLookAt(0,0,-5, 0,0,0, 0, 1, 0)
gluPerspective(45, float(800) / 600, .000001, 75)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glMatrixMode(GL_MODELVIEW)

vertices = [ 0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 1.0, 0.0 ]
vbo = glGenBuffers (1)
glBindBuffer (GL_ARRAY_BUFFER, vbo)
glBufferData (GL_ARRAY_BUFFER, len(vertices)*4, (c_float*len(vertices))(*vertices), GL_STATIC_DRAW)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	glDrawBuffer(GL_BACK)
	glColorMaterial(GL_FRONT, GL_DIFFUSE)
	glClear(GL_COLOR_BUFFER_BIT)

	glBindBuffer (GL_ARRAY_BUFFER, vbo)
	glColor (0.0, 1.0, 1.0, 1.0)
	glVertexPointer (3, GL_FLOAT, 0, 0)
	glDrawArrays (GL_TRIANGLES, 0, 3)
	glClear(GL_DEPTH_BUFFER_BIT)
	glDrawBuffer(GL_FRONT)
	glFlush()
	pygame.display.flip ()
	glBufferData (GL_ARRAY_BUFFER, len(vertices)*4, np.array (vertices, dtype="float32"),GL_STATIC_DRAW)
	glVertexPointer (3, GL_FLOAT, 0, None)
