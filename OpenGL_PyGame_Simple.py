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

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, float(800) / 600, .000001, 75)
gluLookAt(0,0,-5, 0,0,0, 0, 1, 0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glEnable(GL_COLOR_MATERIAL)

glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

glClearColor(.3, .1, .3, 1.0)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	glDrawBuffer(GL_BACK)
	glColor (0.0, 1.0, 1.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT)

	glEnableClientState (GL_VERTEX_ARRAY)
	vertices = [ 0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 1.0, 0.0 ]
	vbo = glGenBuffers (1)
	glBindBuffer (GL_ARRAY_BUFFER, vbo)
	glBufferData (GL_ARRAY_BUFFER, len(vertices)*4, (c_float*len(vertices))(*vertices), GL_STATIC_DRAW)
	glVertexPointer (3, GL_FLOAT, 0, None)
	glPushMatrix()
	glDrawArrays (GL_TRIANGLES, 0, 3)
	glPopMatrix()
	glDisableClientState (GL_VERTEX_ARRAY)

	glDrawBuffer(GL_FRONT)
	glClear(GL_DEPTH_BUFFER_BIT)
	glColor (0.0, 1.0, 1.0, 1.0)

	glFlush()
	pygame.display.flip ()
