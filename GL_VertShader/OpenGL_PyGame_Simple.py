import sys, time
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL.shaders import *
from ctypes import *
import numpy as np
from OpenGLShader import *

w = 1200
h = 600
pygame.init ()
screen = pygame.display.set_mode ((w,h), pygame.HWSURFACE | pygame.OPENGL|pygame.DOUBLEBUF, 24)
glViewport (0, 0, w, h)

glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_POSITION, (.2, .2, -5))

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(50, float(w) / h, .000001, 175)
gluLookAt(0,0,-5, 0,0,0, 0, 1, 0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

glEnable(GL_COLOR_MATERIAL)

glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

glClearColor(.3, .1, .3, 1.0)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

#shaderProgram = shader()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			sys.exit()

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
	#glUseProgram(shaderProgram)
	glDrawArrays (GL_TRIANGLES, 0, 3)
	glPopMatrix()
	glDisableClientState (GL_VERTEX_ARRAY)

	glDrawBuffer(GL_FRONT)
	glClear(GL_DEPTH_BUFFER_BIT)
	glColor (0.0, 1.0, 1.0, 1.0)

	glFlush()
	pygame.display.flip ()
