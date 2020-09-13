# -*- coding: utf-8 -*-
import sys, time
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL.shaders import *
from ctypes import *
import numpy as np
import glm
import random
import array

from SHADER_Primitives import *
from VBO_Primitives import *
from IMAGE_Primitives import *

def init():
	w = 1200
	h = 600
	pygame.init()
	pygame.display.set_mode((w,h), HWSURFACE | OPENGL | DOUBLEBUF)
	glViewport(0, 0, w, h)

	glDisable(GL_DEPTH_TEST)
	glDisable(GL_CULL_FACE)

	lightZeroPosition = [0., -4., 10., 1.]
	lightZeroColor = [0.9, 1.0, 0.9, 1.0]
	glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
	glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
	glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.5)
	glEnable(GL_LIGHT0)

	glEnable(GL_COLOR_MATERIAL)
	glEnable( GL_TEXTURE_2D )
	#glEnable(GL_MULTISAMPLE)
	#glEnable(GL_NORMALIZE)
	glEnable(GL_POINT_SMOOTH)
	glEnable(GL_LINE_SMOOTH)
	glEnable(GL_POLYGON_SMOOTH)
	glEnable(GL_POLYGON_OFFSET_FILL)
	#glEnable(GL_BLEND);
	#glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glShadeModel( GL_SMOOTH )

	glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
	glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
	glLineWidth(1.0)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45, float(w) / h, .000001, 275)
	gluLookAt(0, 0, -5, 0, 0, 0, 0, 1, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def main():
	init()
	f = "../media/girl1.jpg"
	global shaderProgram
	shaderProgram = getShader()
	t, w, h = getTexture(f)
	BindTexture(t, w, h)
	#glUseProgram(shaderProgram)
	VertexAttributes(shaderProgram)
	#tex = getTextureLoc(shaderProgram, 'tex')
	clock = pygame.time.Clock()

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYUP:
				sys.exit()
			if event.type == pygame.K_ESCAPE:
				sys.exit()

		glClearColor(0.0, 0.3, 0.0, 1)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glDrawBuffer(GL_BACK)

		#drawCube()
		#glUseProgram(shaderProgram)
		NormalMapping()
		VBO(1)
		glUseProgram(0)

		pygame.display.flip()

main()
