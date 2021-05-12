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
