import sys
sys.path.append(r"C:\Users\Diego2\Desktop\CORE_COMPILAR\MyTao")

import clr
clr.AddReference("Tao.OpenGl.dll")
clr.AddReference("Tao.FreeGlut.dll")
from System import UInt32, IntPtr
from ctypes import *

import Tao.OpenGl.Gl as Gl
import Tao.OpenGl.Glu as Glu
import Tao.FreeGlut.Glut as Glut

from math import cos,sin,pi
from NP2Interface.NP import *
from GlutControls import *
from GlutWindow import *
from GlutSharedData import *

def our_horizon():
	z = 70
	X = xrange(-30,31,1)
	Y = xrange(-12,3,1)
	for x in X:
		for y in Y:
			Gl.glPushMatrix()
			Gl.glBegin(Gl.GL_POLYGON)
			Gl.glColor3f( 0.1, 0.1, 0.8)
			Gl.glEdgeFlag(True)
			Gl.glVertex3f(-x+0.2, y+0.8, z)
			Gl.glVertex3f(-x+0.8, y+0.8, z)
			Gl.glVertex3f(-x+0.8, y+0.2, z)
			Gl.glVertex3f(-x+0.2, y+0.2, z)
			Gl.glEnd()
			Gl.glPopMatrix()

def our_matrix_world():
	y = -2
	X = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
	Z = [1,2,3,4,5,6,7,8,9,10,11,12]
	for x in X:
		for z in Z:
			Gl.glPushMatrix()
			Gl.glColor3f( 0.0, 0.4, 0.9)
			Gl.glBegin(Gl.GL_POLYGON)
			Gl.glEdgeFlag(True)
			Gl.glVertex3f(-x+0.2, y, z+0.8)
			Gl.glVertex3f(-x+0.8, y, z+0.8)
			Gl.glVertex3f(-x+0.8, y, z+0.2)
			Gl.glVertex3f(-x+0.2, y, z+0.2)
			Gl.glEnd()
			Gl.glPopMatrix()

def our_character():
	A = linspace(0, 2*pi, 4)
	for z in linspace(1, 8, 4):
		for v in A:
			Gl.glPushMatrix()
			Gl.glColor3f( 1.0, 0.0, 0.0)
			Gl.glTranslatef(cos(v), sin(v), z)
			Glut.glutSolidSphere(0.2, 5, 5);
			Gl.glPopMatrix()

def on_display():
	""" Offline OpenGL rendering """
	# TODO fix lookAt, doublebuffers, back-front etc
	lookAt()  ## troubles the doublebuffer
	#Gl.glDrawBuffer(Gl.GL_BACK)
	#Gl.glColorMaterial(Gl.GL_FRONT, Gl.GL_DIFFUSE)
	Gl.glClear(Gl.GL_COLOR_BUFFER_BIT)

	our_horizon()
	our_matrix_world()
	our_character()

	#Gl.glClear(Gl.GL_DEPTH_BUFFER_BIT)
	#Gl.glDrawBuffer(Gl.GL_FRONT)
	#Gl.glFlush()

	# Push offline renders to the videobuffer
	Glut.glutSwapBuffers()

def main():
	Glut.glutInit()
	Glut.glutInitDisplayMode(Glut.GLUT_DOUBLE | Glut.GLUT_RGBA)
	Glut.glutInitWindowPosition(50,30)
	Glut.glutInitWindowSize(1200, 650)
	Glut.glutCreateWindow("Graphic Example")
	init_graphics()
	Glut.glutReshapeFunc(on_reshape)
	Glut.glutDisplayFunc(on_display)

	Glut.glutCloseFunc(on_close)
	Glut.glutKeyboardUpFunc(on_up)
	Glut.glutMouseFunc(mouse_up)
	Glut.glutSpecialUpFunc(special_up)
	Glut.glutMainLoop()

if "__main__" == __name__:
	main()
