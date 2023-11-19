# -*- coding: utf-8 -*-
from AllImports import *
from Init import *

def Scene1():
	spacedSquares()
	drawCube()
	VBO(1)

def main():
	init()
	print(os.getcwd())
	global shaderProgram
	shaderProgram = getShader() # Shaderprogram es always zero. corregir
	f = "media/checkers12.jpg"
	_img = getTexture(f)
	clock = pygame.time.Clock()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYUP:
				pass
			if event.type == pygame.K_ESCAPE:
				sys.exit()

		glClearColor(0.0, 0.3, 0.0, 1)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glDrawBuffer(GL_BACK)

		glUseProgram(0)
		BindTexture(_img.image, _img.width, _img.height)
		tex = getTextureLoc(shaderProgram, 'color')
		VertexAttributes()
		VBO(1)

		pygame.display.flip()

main()
