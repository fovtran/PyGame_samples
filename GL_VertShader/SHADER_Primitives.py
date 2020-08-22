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

from VBO_Primitives import *
from IMAGE_Primitives import *

def getShader():
	shaderProgram = glCreateProgram()

	try:
		vertexShader = compileShader(getFileContent("vertex.vert"), GL_VERTEX_SHADER)
		fragmentShader = compileShader(getFileContent("vertex.frag"), GL_FRAGMENT_SHADER)
		glAttachShader(shaderProgram, vertexShader)
		glAttachShader(shaderProgram, fragmentShader)
		glLinkProgram(shaderProgram)

	except OpenGL.GL.shaders.ShaderCompilationError as e:
		print(e.args[0])
		for a in str(e.args[1]).split(r'\n'):
			print(a)
			pass

	return shaderProgram

def getTexture(fileName):
	img = pygame.image.load(fileName)
	#img = Image.open(filename)
	#img_data = numpy.array(list(img.getdata()), numpy.int8)
	textureData = pygame.image.tostring(img, "RGB", 1)
	width = img.get_width()
	height = img.get_height()

	try:
		texture = FileTexture( fileName )
	except:
		print ('could not open ', fileName, '; using random texture')
		#texture = RandomTexture( 256, 256 )
		texture = textureData

	return texture, width, height

def BindTexture(texture, width, height):
	glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, 1)
	#glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

	#glTexImage2D( GL_TEXTURE_2D, 0, 3, texture.xSize, texture.ySize, 0, GL_RGB, GL_UNSIGNED_BYTE, texture.rawReference )

	#glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	#glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	#glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
	#glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	#glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	#glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
	glTexImage2D( GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture )
	#glGenerateMipmap(GL_TEXTURE_2D)


def VertexAttributes(shaderProgram):
	vertices = [-0.5, -0.5,
	            -0.5, 0.5,
	            0.5, 0.5,
	            0.5, -0.5]

	texcoords = [0.0, 0.0,
	             0.0, 1.0,
	             1.0, 1.0,
	             1.0, 0.0]

	vertices = np.array(vertices, dtype=np.float32)
	texcoords = np.array(texcoords, dtype=np.float32)

	glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, vertices)
	glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 0, texcoords)
	glEnableVertexAttribArray(0)
	glEnableVertexAttribArray(1)

def getTextureLoc(shaderProgram, x):
	glUseProgram(shaderProgram)
	texloc = glGetUniformLocation(shaderProgram, x)
	print(texloc)
	return texloc
