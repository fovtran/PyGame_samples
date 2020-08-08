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

def init():
	w = 1200
	h = 600
	pygame.init()
	pygame.display.set_mode((w,h), HWSURFACE | OPENGL | DOUBLEBUF)
	glViewport(0, 0, w, h)

	glDisable(GL_DEPTH_TEST)
	glDisable(GL_CULL_FACE)

	lightZeroPosition = [10., 4., 10., 1.]
	lightZeroColor = [0.8, 1.0, 0.8, 1.0]
	#glLightfv(GL_LIGHT0, GL_POSITION, (.2, 2, -5))
	glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
	glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
	glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
	glEnable(GL_LIGHT0)

	glEnable(GL_COLOR_MATERIAL)
	glEnable( GL_TEXTURE_2D )
	glEnable(GL_MULTISAMPLE)
	glEnable(GL_NORMALIZE)
	glEnable(GL_POINT_SMOOTH)
	glEnable(GL_LINE_SMOOTH)
	glEnable(GL_POLYGON_SMOOTH)
	glEnable(GL_POLYGON_OFFSET_FILL)
	glEnable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glShadeModel( GL_SMOOTH )

	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
	glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
	glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
	glLineWidth(1.0)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45, float(w) / h, .000001, 275)
	gluLookAt(0, 0, -5, 0, 0, 0, 0, 1, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def drawCube( self ):
	"""Draw a cube with texture coordinates"""
	glBegin(GL_QUADS);
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0);
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0);
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0);
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0);
	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0);
	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0, -1.0);
	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, -1.0);
	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0);
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0);
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0);
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0);
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0);
	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0);
	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0);
	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0);
	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0);
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0);
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0);
	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0);
	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0);
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0);
	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0);
	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0);
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0);
	glEnd()

def main():
	init()
	shaderProgram,tex = shader()

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		glClearColor(0.0, 0.3, 0.0, 1)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		#glDrawBuffer(GL_BACK)
		#glEnableClientState(GL_VERTEX_ARRAY)
		#glPushMatrix()
		#glUniform1i(tex, 0)
		#glColor3f( 1, 0, 0 )
		#glDrawArrays(GL_QUADS, 0, 4)
		#glPopMatrix()
		#glDisableClientState(GL_VERTEX_ARRAY)

		glColor3f( 1.0, 1.0, 1.0)
		y = -2
		X = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
		Z = [1,2,3,4,5,6,7,8,9,10,11,12]
		for x in X:
			for z in Z:
				glPushMatrix()
				glBegin(GL_QUADS)
				glTexCoord2f( 0, 1 )
				glVertex3f(-x+0.2, y, z+0.8)
				glTexCoord2f( 0, 0 )
				glVertex3f(-x+0.8, y, z+0.8)
				glTexCoord2f( 1, 0 )
				glVertex3f(-x+0.8, y, z+0.2)
				glTexCoord2f( 1, 1 )
				glVertex3f(-x+0.2, y, z+0.2)
				glEnd()
				glPopMatrix()

		glBegin( GL_QUADS )
		glTexCoord2f( 0, 1 )
		glVertex3f( -0.5, 0.5, 0 )
		glTexCoord2f( 0, 0 )
		glVertex3f( -0.5, -0.5, 0 )
		glTexCoord2f( 1, 0 )
		glVertex3f( 0.5, -0.5, 0 )
		glTexCoord2f( 1, 1 )
		glVertex3f( 0.5, 0.5, 0 )
		glEnd(  )

		glUseProgram(0)
		pygame.display.flip()

main()
