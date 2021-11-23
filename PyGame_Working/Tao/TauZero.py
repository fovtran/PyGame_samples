import sys,os
sys.path.insert(0,r"C:\Users\Diego2\Desktop\CORE_COMPILAR\MyTao\libs")
sys.path.append(os.path.dirname(__file__))

import clr
a = sys.version.split()

if a[0].startswith('3'):
	print('Python Interpreter detected')

if a[0].startswith('2'):
	print('IronPython Interpreter detected')
	clr.AddReferenceToFile("./libs/Tao.OpenGl.dll")
	clr.AddReferenceToFile("./libs/Tao.FreeGlut.dll")

# from System import UInt32, IntPtr
from ctypes import *

from Tao.OpenGl.Gl import *
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
			glPushMatrix()
			glBegin(GL_POLYGON)
			glColor3f( 0.1, 0.1, 0.8)
			glEdgeFlag(True)
			glVertex3f(-x+0.2, y+0.8, z)
			glVertex3f(-x+0.8, y+0.8, z)
			glVertex3f(-x+0.8, y+0.2, z)
			glVertex3f(-x+0.2, y+0.2, z)
			glEnd()
			glPopMatrix()

def our_matrix_world():
	y = -2
	X = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
	Z = [1,2,3,4,5,6,7,8,9,10,11,12]
	for x in X:
		for z in Z:
			glPushMatrix()
			glColor3f( 0.0, 0.4, 0.9)
			glBegin(GL_POLYGON)
			glEdgeFlag(True)
			glVertex3f(-x+0.2, y, z+0.8)
			glVertex3f(-x+0.8, y, z+0.8)
			glVertex3f(-x+0.8, y, z+0.2)
			glVertex3f(-x+0.2, y, z+0.2)
			glEnd()
			glPopMatrix()

def our_character():
	A = linspace(0, 2*pi, 4)
	for z in linspace(1, 8, 4):
		for v in A:
			glPushMatrix()
			glColor3f( 1.0, 0.0, 0.0)
			glTranslatef(cos(v), sin(v), z)
			Glut.glutSolidSphere(0.2, 5, 5);
			glPopMatrix()

def on_display():
	""" Offline OpenGL rendering """
	# TODO fix lookAt, doublebuffers, back-front etc
	lookAt()  ## troubles the doublebuffer
	#glDrawBuffer(GL_BACK)
	#glColorMaterial(GL_FRONT, GL_DIFFUSE)
	Gl.glClear(Gl.GL_COLOR_BUFFER_BIT)

	our_horizon()
	our_matrix_world()
	our_character()

	#glClear(GL_DEPTH_BUFFER_BIT)
	#glDrawBuffer(GL_FRONT)
	#glFlush()

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
