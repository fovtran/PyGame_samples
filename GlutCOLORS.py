import clr
clr.AddReferenceToFile("./libs/Tao.OpenGl.dll")
clr.AddReferenceToFile("./libs/Tao.FreeGlut.dll")

from System import UInt32, IntPtr
from ctypes import *

import Tao.OpenGl.Gl as Gl
import Tao.OpenGl.Glu as Glu
import Tao.FreeGlut.Glut as Glut


def pusher():

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

def green():
	green = (0.0, 1.0, 0.0)
	Gl.glMaterialfv (Gl.GL_FRONT, Gl.GL_AMBIENT_AND_DIFFUSE, green)
def red():
	red = (1.0, 0.0, 0.0 )
	Gl.glMaterialfv (Gl.GL_FRONT, Gl.GL_AMBIENT_AND_DIFFUSE, red)
def blue():
	blue = (0.0, 0.0, 1.0 )
	Gl.glMaterialfv (Gl.GL_FRONT, Gl.GL_AMBIENT_AND_DIFFUSE, blue)
def yellow():
	yellow = (1.0, 0.94, 0.045 )
	Gl.glMaterialfv (Gl.GL_FRONT, Gl.GL_AMBIENT_AND_DIFFUSE, yellow)
