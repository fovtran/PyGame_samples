import clr
clr.AddReferenceToFile("Tao.OpenGl.dll")
clr.AddReferenceToFile("Tao.FreeGlut.dll")
from System import UInt32, IntPtr
from ctypes import *

import Tao.OpenGl.Gl as Gl
import Tao.OpenGl.Glu as Glu
import Tao.FreeGlut.Glut as Glut

from math import cos,sin,pi
from NP2Interface.NP import *

def init_graphics():
	Gl.glEnable(Gl.GL_LIGHTING)
	Gl.glEnable(Gl.GL_LIGHT0)
	Gl.glLightfv(Gl.GL_LIGHT0, Gl.GL_POSITION, (.2, .2, -5))
	Gl.glEnable(Gl.GL_COLOR_MATERIAL)
	Gl.glClearColor(.3, .1, .3, 1.0)
	Gl.glPolygonMode(Gl.GL_FRONT_AND_BACK, Gl.GL_LINE)
	Gl.glHint(Gl.GL_LINE_SMOOTH_HINT, Gl.GL_NICEST)

def on_display():
	Gl.glLoadIdentity()
	Glu.gluLookAt(0, 0, -5, 0, 0, 0, 0, 1, 0)
	Gl.glDrawBuffer(Gl.GL_BACK)
	Gl.glLineWidth(1.0)
	Gl.glColorMaterial(Gl.GL_FRONT, Gl.GL_DIFFUSE)

	Gl.glClear(Gl.GL_COLOR_BUFFER_BIT)

	A = linspace(0, 2*pi, 4)
	for z in linspace(1, 10, 5):
		for v in A:
			Gl.glPushMatrix()
			Gl.glColor3f( 1.0, 0.0, 0.0)
			Gl.glTranslatef(cos(v), sin(v), z)
			Glut.glutWireSphere(0.2, 5, 5);
			Gl.glPopMatrix()
			#Gl.glPushMatrix()
			#Gl.glBegin(Gl.GL_POINTS)
			#Gl.glEdgeFlag(True)
			#Gl.glVertex3f(cos(v), sin(v), z)
			#Gl.glEnd()
			#Gl.glPopMatrix()
	Gl.glClear(Gl.GL_DEPTH_BUFFER_BIT)
	Gl.glDrawBuffer(Gl.GL_FRONT)
	Gl.glFlush()
	Glut.glutSwapBuffers()

def on_reshape(w, h):
	Gl.glMatrixMode(Gl.GL_PROJECTION)
	Gl.glLoadIdentity()
	Gl.glViewport(0, 0, w, h)
	Glu.gluPerspective(50, float(w) / h, .000001, 10)
	Gl.glClear(Gl.GL_COLOR_BUFFER_BIT | Gl.GL_DEPTH_BUFFER_BIT)
	Gl.glMatrixMode(Gl.GL_MODELVIEW)
	#Gl.glMatrixMode(Gl.GL_COLOR)

def main():
	Glut.glutInit()
	Glut.glutInitDisplayMode(Glut.GLUT_DOUBLE | Glut.GLUT_RGBA)
	Glut.glutInitWindowSize(800, 600)
	Glut.glutCreateWindow("TAU Graphic Example")
	init_graphics()
	Glut.glutDisplayFunc(on_display)
	Glut.glutReshapeFunc(on_reshape)
	Glut.glutMainLoop()

if "__main__" == __name__:
	main()
