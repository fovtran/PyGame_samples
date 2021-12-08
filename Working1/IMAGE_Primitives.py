# -*- coding: utf-8 -*-
from AllImports import *

from SHADER_Primitives import *
from VBO_Primitives import *

class image:
    img = ""
    width = 0
    height = 0

def getTexture(fileName):
    #img = Image.open(filename)
    #img_data = numpy.array(list(img.getdata()), numpy.int8)
    _img = image()

    try:
        img = pygame.image.load(fileName)
        _img.image = rawTextureData = pygame.image.tostring(img, "RGB", 1)
        _img.width = img.get_width()
        _img.height = img.get_height()
    except:
        print ('could not open ', fileName, '; using random texture')
        #texture = RandomTexture( 256, 256 )
    return _img

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
