# -*- coding: utf-8 -*-
from AllImports import *

from VBO_Primitives import *
from IMAGE_Primitives import *

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

def getFileContent(file):
    pathname = os.path.dirname(sys.argv[0])
    fullpath = os.path.abspath(pathname)
    filename = os.path.join(fullpath, file)
    content = open(filename, 'r').read()
    return content

def getShader():
	shaderProgram = glCreateProgram()

	try:
		vertexShader = compileShader(getFileContent("shaders/vertex.vert"), GL_VERTEX_SHADER) # TODO: RESUMIR
		fragmentShader = compileShader(getFileContent("shaders/vertex.frag"), GL_FRAGMENT_SHADER)
		glAttachShader(shaderProgram, vertexShader)
		glAttachShader(shaderProgram, fragmentShader)
		glLinkProgram(shaderProgram)

	except OpenGL.GL.shaders.ShaderCompilationError as e:
		print(e.args[0])
		for a in str(e.args[1]).split(r'\n'):
			print(a)

	return shaderProgram # Devuelve shader zero. corregir.

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

