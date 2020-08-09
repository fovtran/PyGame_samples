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


def VBO(tex):
	#glColor3f( 1, 0, 0 )
	glEnableClientState(GL_VERTEX_ARRAY)
	glPushMatrix()
	glDrawArrays(GL_QUADS, 0, 4)
	glPopMatrix()
	glDisableClientState(GL_VERTEX_ARRAY)

def NormalMapping():
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

def drawCube():
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
