import clr
clr.AddReferenceToFile("Tao.OpenGl.dll")
clr.AddReferenceToFile("Tao.FreeGlut.dll")
from System import UInt32, IntPtr
from ctypes import *

import Tao.OpenGl.Gl as Gl
import Tao.OpenGl.Glu as Glu
import Tao.FreeGlut.Glut as Glut
from GlutCOLORS import *

def init_graphics():
	Gl.glEnable(Gl.GL_LIGHTING)
	Gl.glEnable(Gl.GL_LIGHT0)
	Gl.glLightfv(Gl.GL_LIGHT0, Gl.GL_POSITION, (.2, .2, -5))

	Gl.glLineWidth(1.0)
	Gl.glPolygonMode(Gl.GL_FRONT_AND_BACK, Gl.GL_FILL)

	Gl.glEnable(Gl.GL_COLOR_MATERIAL)
	Gl.glColorMaterial(Gl.GL_FRONT_AND_BACK, Gl.GL_AMBIENT_AND_DIFFUSE)

	mat_ambient = (0.7, 0.0, 0.0, 1.0)
	mat_diffuse= (0.3, 0.0, 0.0, 1.0)
	mat_specular = (0.0, 0.0, 0.0, 0.0)
	mat_shininess = (1.8)

	Gl.glMaterialfv(Gl.GL_FRONT, Gl.GL_AMBIENT, mat_ambient)
	Gl.glMaterialfv(Gl.GL_FRONT, Gl.GL_DIFFUSE, mat_diffuse)
	Gl.glMaterialfv(Gl.GL_FRONT, Gl.GL_SPECULAR, mat_specular)
	Gl.glMaterialfv(Gl.GL_FRONT, Gl.GL_SHININESS, mat_shininess)
	Gl.glDisable(Gl.GL_COLOR_MATERIAL)

def pusher():
	lDList = Gl.glGenLists(1)
	Gl.glNewList(lDList, Gl.GL_COMPILE)
	Gl.glBegin(Gl.GL_QUADS)
	yellow()
	Gl.glVertex3i(-1, -1, 0)
	Gl.glVertex3i(1, -1, 0)
	Gl.glVertex3i(1, -1, -2)
	Gl.glVertex3i(-1, -1, -2)
	Gl.glEnd()
	Gl.glEndList()
	Gl.glPushMatrix()
	Gl.glLineWidth(10)
	Gl.glPolygonMode(Gl.GL_FRONT_AND_BACK, Gl.GL_LINES)
	Gl.glColor3f(0, 0, 0)
	Gl.glCallList(lDList)
	Gl.glCallList(lDList);
	Gl.glPolygonMode(Gl.GL_FRONT_AND_BACK, Gl.GL_FILL)
	Gl.glPopMatrix()

def on_display():
	Gl.glLoadIdentity()
	Glu.gluLookAt(0, 0, -5, 0, 0, 0, 0, 1, 0)
	#Gl.glClear(Gl.GL_COLOR_BUFFER_BIT | Gl.GL_DEPTH_BUFFER_BIT)
	Gl.glClearColor(.3, .1, .3, 1.0)
	Gl.glDrawBuffer(Gl.GL_FRONT)
	Gl.glClear(Gl.GL_COLOR_BUFFER_BIT)

	pusher()

	Gl.glPushMatrix()
	Gl.glBegin(Gl.GL_POLYGON)
	blue()
	Gl.glVertex3f(0.5, 1.3, 0)
	Gl.glVertex3f(1.4, 1.3, 0)
	Gl.glVertex3f(1.4, 0.3, 0)
	Gl.glVertex3f(0.5, 0.3, 0)
	Gl.glEnd()
	Gl.glPopMatrix()

	Gl.glFlush()
	Glut.glutSwapBuffers()

	Gl.glDrawBuffer(Gl.GL_BACK)
	Gl.glPushMatrix()
	green()
	Gl.glBegin(Gl.GL_POLYGON)
	Gl.glEdgeFlag(True)
	Gl.glVertex3f(0.1, 0.3, 0)
	Gl.glVertex3f(0.4, -1.3, 0)
	Gl.glVertex3f(2.2, -0.3, 0)
	Gl.glEnd()
	Gl.glPopMatrix()

	Gl.glPushMatrix()
	Gl.glBegin(Gl.GL_TRIANGLES)
	red()
	Gl.glVertex3f(0.5, 1.3, 0)
	Gl.glVertex3f(1.4, 1.3, 0)
	Gl.glVertex3f(1.4, 0.3, 0)
	Gl.glVertex3f(0.5, 0.3, 0)
	Gl.glEnd()
	Gl.glPopMatrix()

	Gl.glFlush()
	Glut.glutSwapBuffers()

def on_reshape(w, h):
	Gl.glMatrixMode(Gl.GL_PROJECTION)
	Gl.glLoadIdentity()
	Gl.glViewport(0, 0, w, h)
	Glu.gluPerspective(50, float(w) / h, .000001, 10)
	Gl.glMatrixMode(Gl.GL_MODELVIEW)
	Gl.glLoadIdentity()

def main():
	Glut.glutInit()
	Glut.glutInitDisplayMode(Glut.GLUT_DEPTH | Glut.GLUT_DOUBLE | Glut.GLUT_RGBA)
	Glut.glutInitWindowSize(1200, 600)
	Glut.glutCreateWindow("Tao Example")
	for x in Gl.glGetString(Gl.GL_EXTENSIONS).split(): print(x)
	init_graphics()
	Glut.glutDisplayFunc(on_display)
	Glut.glutReshapeFunc(on_reshape)
	Glut.glutMainLoop()

if "__main__" == __name__:
	main()
