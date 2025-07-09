# -*- coding: utf-8 -*-
from AllImports import *

from GITCLONE.PyGame_samples.Working1.ShaderPrimitives import *
from GITCLONE.PyGame_samples.Working1.VertexBufferPrimitives import *
from GITCLONE.PyGame_samples.Working1.ImagePrimitives import *

def VertexAttributes():
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

def VBO(tex):
	# Nuestro Vertex Buffer esta Vacio. corregir
	# Color morado significa que nuestro quads no tiene vertices de textura asignados.
	#glColor3f( 1, 0, 0 )
	glEnableClientState(GL_VERTEX_ARRAY)
	glPushMatrix()
	glDrawArrays(GL_QUADS, 0, 7)
	glPopMatrix()
	glDisableClientState(GL_VERTEX_ARRAY)

def spacedSquares():
	# Cambiar nombre de funcion
	glColor3f( 1.0, 1.0, 1.0)
	y = -2
	X = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
	Z = [1,2,3,4,5,6,7,8,9,10,11]
	for x in X:
		for z in Z:
			glPushMatrix()
			glBegin(GL_QUADS)
			glTexCoord2f( 0, 1 )
			glVertex3f(-x+0.2, y, z+0.8)
			glTexCoord2f( 0, 0 )
			glVertex3f(-x+0.8, y, z+0.8)
			glTexCoord2f( 1, 0 )
			glVertex3f(-x+0.8, y, z+0.2)
			glTexCoord2f( 1, 1 )
			glVertex3f(-x+0.2, y, z+0.2)
			glEnd()
			glPopMatrix()

def drawCube():
	glBegin(GL_QUADS);
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0);
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0);
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0);
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0);


	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0);
	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0, -1.0);
	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, -1.0);
	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0);
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0);
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0);
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0);
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0);
	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0);
	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0);
	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0);
	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0);
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0);
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0);
	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0);
	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0);
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0);
	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0);
	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0);
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0);
	glEnd()
