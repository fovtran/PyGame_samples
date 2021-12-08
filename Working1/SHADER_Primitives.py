# -*- coding: utf-8 -*-
from AllImports import *

from VBO_Primitives import *
from IMAGE_Primitives import *

def getShader():
	shaderProgram = glCreateProgram()

	try:
		vertexShader = compileShader(getFileContent("shaders\\vertex.vert"), GL_VERTEX_SHADER) # TODO: RESUMIR
		fragmentShader = compileShader(getFileContent("shaders\\vertex.frag"), GL_FRAGMENT_SHADER)
		glAttachShader(shaderProgram, vertexShader)
		glAttachShader(shaderProgram, fragmentShader)
		glLinkProgram(shaderProgram)

	except OpenGL.GL.shaders.ShaderCompilationError as e:
		print(e.args[0])
		for a in str(e.args[1]).split(r'\n'):
			print(a)

	return shaderProgram # Devuelve shader zero. corregir.

def BindTexture(texture, width, height):
	Tx = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, Tx)
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
	glTexImage2D( GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture ) #INVESTIGAR
	#glGenerateMipmap(GL_TEXTURE_2D)

def getTextureLoc(shaderProgram, x):
	glUseProgram(shaderProgram)
	return glGetUniformLocation(shaderProgram, x)
