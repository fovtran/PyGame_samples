import clr
clr.AddReferenceToFile("Tao.OpenGl.dll")
clr.AddReferenceToFile("Tao.FreeGlut.dll")
from System import UInt32, IntPtr
from ctypes import *

import Tao.OpenGl.Gl as Gl
import Tao.OpenGl.Glu as Glu
import Tao.FreeGlut.Glut as Glut

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
