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
FPS = 10

def pygame_init():
	global screen
	pygame.init ()
	pygame.font.init()
	info = pygame.display.Info()
	print(info)
	flags = pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE | pygame.SRCALPHA
	screen = pygame.display.set_mode ((w,h),flags, 24, vsync=0)
	glViewport (0, 0, w, h)

	lightZeroPosition = [0., -4., 10., 1.]
	lightZeroColor = [0.9, 1.0, 0.9, 1.0]
	glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
	glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.05)
	glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
	glEnable(GL_LIGHT0)
	glLightfv(GL_LIGHT0, GL_POSITION, (.2, .2, -45))

	glDisable(GL_DEPTH_TEST)
	glDisable(GL_CULL_FACE)

	glEnable(GL_COLOR_MATERIAL)
	glEnable( GL_TEXTURE_2D )
	glDisable(GL_MULTISAMPLE)
	#glEnable(GL_NORMALIZE)
	glEnable(GL_POINT_SMOOTH)
	glEnable(GL_LINE_SMOOTH)
	glEnable(GL_POLYGON_SMOOTH)
	glEnable(GL_POLYGON_OFFSET_FILL)
	glDisable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glShadeModel( GL_SMOOTH )

	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
	glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

	glClearColor(.05, .05, .05, 1.0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
	return screen

def VBO():
	glEnableClientState (GL_VERTEX_ARRAY)
	vertices = [ 0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 1.0, 0.0 ]
	vbo = glGenBuffers (1)
	glBindBuffer (GL_ARRAY_BUFFER, vbo)
	glBufferData (GL_ARRAY_BUFFER, len(vertices)*4, (c_float*len(vertices))(*vertices), GL_STATIC_DRAW)
	glVertexPointer (3, GL_FLOAT, 0, None)
	glPushMatrix()
	glColor (0.05, 0.95, 0.05, 1.0)
	glDrawArrays (GL_TRIANGLES, 0, 3)
	#glPopMatrix()
	glDisableClientState (GL_VERTEX_ARRAY)

running = True
pygame_init()

color_dark = (2,2,2,255)
global LD
LD = glGenLists(4)
LD_2D=LD+1
LD_3D=LD+2
LD_4D=LD+3
LD_CL=LD+4

glNewList(LD, GL_COMPILE)
glLoadIdentity()
VBO()
glEndList()

glNewList(LD_CL, GL_COMPILE)
glEndList()

glNewList(LD_2D, GL_COMPILE)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0,w,0,h, 0.1, 1000)
gluLookAt(0,0,-5, 0,0,0, 0, 1, 0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glEndList()

glNewList(LD_3D, GL_COMPILE)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(85.0,float(w)/float(h), 0.1, 1000)
gluLookAt(0,0,-5, 0,0,0, 0, 1, 0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glEndList()

glNewList(LD_4D, GL_COMPILE)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(85, float(w) / h, .000001, 1000)
gluLookAt(0,0,-5, 0,0,0, 0, 1, 0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glEndList()

# store current matrix
glMatrixMode( GL_MODELVIEW );
glLoadIdentity();
glPushMatrix( );

# restore current matrix
glMatrixMode( GL_MODELVIEW );
glPopMatrix( );

def Controls():
	if True:
		for event in pygame.event.get():
			if event.type == pygame.KEYUP:	glCallList(LD_2D);glLoadIdentity()
			if event.type == pygame.KEYDOWN:	glCallList(LD_3D)
			if event.type == pygame.K_LEFT:	glCallList(LD_4D)
			if event.type == pygame.K_RIGHT:	glCallList(LD_CL)
			if event.type == pygame.QUIT:	pygame.quit()
			if event.type == pygame.K_SPACE:	pygame.quit()

clock = pygame.time.Clock()
color = pygame.Color('white')
#start_button = pygame.draw.rect(surface,(0,0,240),(150,90,100,50));
#quit_button = pygame.draw.rect(surface,(244,0,0),(150,230,100,50));
surface = pygame.Surface(( round(w/2)+50, round(h/2) ), flags=pygame.SRCALPHA)
rect = pygame.draw.rect(surface, color, [0,0,40,40])

smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('quit' , 0, color)
text.set_alpha(100)
surface.fill(color)

#pygame.display.update()

while running:
	dt = clock.tick(FPS) / 1000
	Controls()
	glClear(GL_COLOR_BUFFER_BIT)
	glCallList(LD_CL)
	glDrawBuffer(GL_BACK)
	glCallList(LD_4D)
	glCallList(LD)
	#glDrawBuffer(GL_FRONT)
	surface.blit(text, (100,0))
	pygame.display.flip ()
	pygame.time.wait(10)
	glFlush()
