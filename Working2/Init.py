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

w = 1200
h = 600
FPS = 10

def SetScreen():
	global screen
	pygame.init ()
	pygame.font.init()
	info = pygame.display.Info()
	print(info)
	flags = pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE
	screen = pygame.display.set_mode((w,h), flags, 32, vsync=0)
	glViewport (0, 0, w, h)
	return screen

def SetLights():
	lightZeroPosition = [0., -4., 10., 1.]
	lightZeroColor = [0.9, 1.0, 0.9, 1.0]
	glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
	glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.05)
	glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
	glEnable(GL_LIGHT0)

def pygame_init():
	screen = SetScreen()
	SetLights()

	glEnable(GL_DEPTH_TEST)
	glDisable(GL_CULL_FACE)

	glEnable(GL_COLOR_MATERIAL)
	glEnable( GL_TEXTURE_2D )
	glDisable(GL_MULTISAMPLE)
	#glEnable(GL_NORMALIZE)
	glEnable(GL_POINT_SMOOTH)
	glEnable(GL_LINE_SMOOTH)
	glEnable(GL_POLYGON_SMOOTH)
	glEnable(GL_POLYGON_OFFSET_FILL)
	glEnable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glShadeModel( GL_SMOOTH )

	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
	glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

	glClearColor(.05, .05, .05, 1.0)
	glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
	# pygame.display.update()
	return screen