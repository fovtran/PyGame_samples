import sys, time
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL.shaders import *
from ctypes import *
#from OpenGLShader import *
import numpy as np

w = 1200
h = 600

def pygame_init():
	global screen,text
	pygame.init ()
	screen = pygame.display.set_mode ((w,h), pygame.HWSURFACE | pygame.OPENGL|pygame.DOUBLEBUF, 24)
	glViewport (0, 0, w, h)

	start_button = pygame.draw.rect(screen,(0,0,240),(150,90,100,50));
	continue_button = pygame.draw.rect(screen,(0,244,0),(150,160,100,50));
	quit_button = pygame.draw.rect(screen,(244,0,0),(150,230,100,50));
	smallfont = pygame.font.SysFont('Corbel',35)
	color = (0,255,0,255)
	text = smallfont.render('quit' , True , color)
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

def VBO():
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

running = True
pygame_init()
color_dark = (254,10,65)
global LD
LD = glGenLists(3)
LD_2D=LD+1
LD_3D=LD+2
LD_CL=LD+3
glNewList(LD, GL_COMPILE)
VBO()
glEndList()

glNewList(LD_CL, GL_COMPILE)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glLoadIdentity()
glEndList()

glNewList(LD_2D,GL_COMPILE)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0,w,0,h, 0.1, 1000)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glEndList()

glNewList(LD_3D, GL_COMPILE)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45.0,float(w)/float(h),0.1,100.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glEndList()

while running:
	for event in pygame.event.get():
		if event.type == pygame.KEYUP:
			glCallList(LD_2D)
		if event.type == pygame.KEYDOWN:
			glCallList(LD_3D)

		if event.type == pygame.QUIT:
			running=False
			sys.exit()
		if event.type == pygame.K_ESCAPE:
			running=False
			sys.exit()

	glDrawBuffer(GL_BACK)
	glClear(GL_COLOR_BUFFER_BIT)
	glColor (0.0, 1.0, 1.0, 1.0)


	glCallList(LD)
	pg_screen = pygame.Surface((w,h), flags=pygame.SRCALPHA)
	pygame.draw.rect(screen,color_dark,[round(w/2),round(h/2),140,40])
	pg_screen.blit(text , ( round(w/2)+50, round(h/2) ) )

	glDrawBuffer(GL_FRONT)
	glClear(GL_DEPTH_BUFFER_BIT)
	glColor (0.0, 1.0, 1.0, 1.0)

	glFlush()
	pygame.display.flip ()
