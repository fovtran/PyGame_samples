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
import random
import array

class Texture( object ):
        """Texture either loaded from a file or initialised with random colors."""
        def __init__( self ):
                self.xSize, self.ySize = 0, 0
                self.rawRefence = None

class RandomTexture( Texture ):
        """Image with random RGB values."""
        def __init__( self, xSizeP, ySizeP ):
                self.xSize, self.ySize = xSizeP, ySizeP
                tmpList = [ random.randint(0, 255) \
                        for i in range( 3 * self.xSize * self.ySize ) ]
                self.textureArray = array.array( 'B', tmpList )
                self.rawReference = self.textureArray.tostring( )

class FileTexture( Texture ):
        """Texture loaded from a file."""
        def __init__( self, fileName ):
                im = Image.open( fileName )
                self.xSize = im.size[0]
                self.ySize = im.size[1]
                self.rawReference = im.tostring("raw", "RGB", 0, -1)

def getFileContent(file):
	content = open(file, 'r').read()
	return content

def shader():
	global shaderProgram
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

	# ----------------------------------------------------

	fileName = "../girl1.jpg"
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

	glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, 1)
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

	#glTexImage2D( GL_TEXTURE_2D, 0, 3, texture.xSize, texture.ySize, 0, GL_RGB, GL_UNSIGNED_BYTE, texture.rawReference )
	glTexImage2D( GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture )

	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
	glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
	#glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	#glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
	glGenerateMipmap(GL_TEXTURE_2D)

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

	glUseProgram(shaderProgram)
	r = glGetProgramInfoLog(shaderProgram)
	print(r)

	global texLocation
	texloc = glGetUniformLocation(shaderProgram, "tex")
	print(texloc)
	return shaderProgram, texloc
