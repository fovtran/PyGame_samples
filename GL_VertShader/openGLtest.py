from OpenGL.GL import *
from OpenGL.GL.shaders import *

import pygame
from pygame.locals import *
import numpy, time, sys

def getFileContent(file):
    content = open(file, 'r').read()
    return content

def init():
    pygame.init()
    pygame.display.set_mode((640, 480), HWSURFACE | OPENGL | DOUBLEBUF)
    glViewport(0, 0, 640, 480)

    img = pygame.image.load("../girl1.jpg")
    textureData = pygame.image.tostring(img, "RGB", 1)
    width = img.get_width()
    height = img.get_height()
    #glGenTextures(1)
    #glBindTexture(GL_TEXTURE_2D, 1)
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

    vertices = numpy.array(vertices, dtype=numpy.float32)
    texcoords = numpy.array(texcoords, dtype=numpy.float32)

    vertexShader = compileShader(getFileContent("helloTriangle.vert"), GL_VERTEX_SHADER)
    fragmentShader = compileShader(getFileContent("helloTriangle.frag"), GL_FRAGMENT_SHADER)

    global shaderProgram
    shaderProgram = glCreateProgram()
    glAttachShader(shaderProgram, vertexShader)
    glAttachShader(shaderProgram, fragmentShader)
    glLinkProgram(shaderProgram)

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, vertices)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 0, texcoords)
    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)

    global texLocation
    texLocation = glGetUniformLocation(shaderProgram, "textureObj")

def main():
    init()

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
