# Copyright (c) 2013 Ashwin Nanjappa
import clr
clr.AddReferenceToFile("Tao.OpenGl.dll")
clr.AddReferenceToFile("Tao.FreeGlut.dll")
from System import UInt32, IntPtr
from ctypes import *

import Tao.OpenGl.Gl as Gl
import Tao.OpenGl.Glu as Glu
import Tao.FreeGlut.Glut as Glut

def init_graphics():
	Gl.glEnable(Gl.GL_LIGHTING)
	Gl.glEnable(Gl.GL_LIGHT0)
	Gl.glLightfv(Gl.GL_LIGHT0, Gl.GL_POSITION, (.2, .2, -5))
	Gl.glEnable(Gl.GL_COLOR_MATERIAL)
	Gl.glClearColor(.3, .1, .3, 1.0)
	Gl.glPolygonMode(Gl.GL_FRONT_AND_BACK, Gl.GL_LINE)

def on_display():
	Gl.glLoadIdentity()
	Glu.gluLookAt(0, 0, -5, 0, 0, 0, 0, 1, 0)
	Gl.glDrawBuffer(Gl.GL_BACK)
	Gl.glLineWidth(1.0)
	Gl.glColorMaterial(Gl.GL_FRONT, Gl.GL_DIFFUSE)

	Gl.glClear(Gl.GL_COLOR_BUFFER_BIT)

	Gl.glPushMatrix()
	Gl.glBegin(Gl.GL_POLYGON)
	Gl.glEdgeFlag(True)
	Gl.glColor3f( 0.0, 0.8, 0.0)
	Gl.glVertex3f(0.1, 0.3, 0)
	Gl.glColor3f( 0.0, 0.8, 0.0)
	Gl.glVertex3f(0.4, -1.3, 0)
	Gl.glColor3f( 0.7, 0.5, 0.3)
	Gl.glVertex3f(2.2, -0.3, 0)
	Gl.glEnd()
	Gl.glPopMatrix()

	Gl.glPushMatrix()
	Gl.glColor3f( 0.0, 0.8, 0.0)
	Gl.glBegin(Gl.GL_TRIANGLES)
	Gl.glEdgeFlag(True)
	Gl.glVertex3f(0.5, 1.3, 0)
	Gl.glVertex3f(1.4, 1.3, 0)
	Gl.glVertex3f(1.4, 0.3, 0)
	Gl.glVertex3f(0.5, 0.3, 0)
	Gl.glEnd()
	Gl.glPopMatrix()

	Gl.glPushMatrix()
	Gl.glColor3f( 0.0, 0.8, 0.0)
	Gl.glBegin(Gl.GL_POLYGON)
	Gl.glEdgeFlag(True)
	Gl.glVertex3f(0.5, 1.3, 0)
	Gl.glVertex3f(1.4, 1.3, 0)
	Gl.glVertex3f(1.4, 0.3, 0)
	Gl.glVertex3f(0.5, 0.3, 0)
	Gl.glEnd()
	Gl.glPopMatrix()

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
	#Glut.glutInitDisplayMode(Glut.GLUT_DEPTH | Glut.GLUT_DOUBLE | Glut.GLUT_RGBA)
	Glut.glutInitDisplayMode(Glut.GLUT_DOUBLE | Glut.GLUT_RGBA)
	Glut.glutInitWindowSize(500, 500)
	Glut.glutCreateWindow("Tao Example")
	#a = Gl.glGetString(Gl.GL_EXTENSIONS)
	#for x in a.split():    print(x)
	init_graphics()
	Glut.glutDisplayFunc(on_display)
	Glut.glutReshapeFunc(on_reshape)
	Glut.glutMainLoop()

if "__main__" == __name__:
	main()
