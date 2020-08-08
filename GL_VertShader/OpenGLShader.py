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

def getFileContent(file):
	content = open(file, 'r').read()
	return content

def shader():
	img = pygame.image.load("../girl1.jpg")
	textureData = pygame.image.tostring(img, "RGB", 1)
	width = img.get_width()
	height = img.get_height()

	glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, 1)
	glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

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

	vert = """
	#version 120
	uniform mat4 projTrans;
	uniform mat4 u_projView;
	attribute vec2 Position;
	attribute vec2 TexCoord;
	varying vec2 vTexCoord;
	void main() { vTexCoord = TexCoord; gl_Position = u_projView * vec4(Position, 0.0, 1.0); }
	"""
	frag = """
	#version 120
	uniform sampler2D tex0;
	varying vec2 vTexCoord;
	void main() {  vec4 color = texture2D(tex0, vTexCoord); gl_FragColor = color; }
	"""
	global shaderProgram
	shaderProgram = glCreateProgram()

	try:
		vertexShader = compileShader(getFileContent("helloTriangle.vert"), GL_VERTEX_SHADER)
		fragmentShader = compileShader(getFileContent("helloTriangle.frag"), GL_FRAGMENT_SHADER)
		glAttachShader(shaderProgram, vertexShader)
		glAttachShader(shaderProgram, fragmentShader)
		glLinkProgram(shaderProgram)
		r = glGetProgramInfoLog(shaderProgram)
		print(r)
	except OpenGL.GL.shaders.ShaderCompilationError as e:
		print(e.args[0])
		for a in str(e.args[1]).split(r'\n'):
			print(a)
	#vertexShader = compileShader(vert, GL_VERTEX_SHADER)
	#fragmentShader = compileShader(frag, GL_FRAGMENT_SHADER)

	glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, vertices)
	glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 0, texcoords)
	glEnableVertexAttribArray(0)
	glEnableVertexAttribArray(1)

	global texLocation
	#texLocation = glGetUniformLocation(shaderProgram, "tex")
	return shaderProgram
