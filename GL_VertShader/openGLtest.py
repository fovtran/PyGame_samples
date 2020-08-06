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
    glViewport(0, 0, w,h)

	#glGenTextures(1)
	#glBindTexture(GL_TEXTURE_2D, 1)

def main():
    init()
	shader()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        glClearColor(0.25, 0.25, 0.25, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glUseProgram(shaderProgram)
        #glUniform1i(texLocation, 0)
        glDrawArrays(GL_QUADS, 0, 4)

        pygame.display.flip()

main()
