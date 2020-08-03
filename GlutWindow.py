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
from NP import *
from GlutControls import *
from GlutSharedData import *

def lookAt():
	cam = camera()
	# eyeX, eyeY, eyeZ          -> eye point.
	# centerX, centerY, centerZ -> target reference point.
	# upX, upY, upZ             -> the up vector.
	Glu.gluLookAt(cam.eyeX, cam.eyeY, cam.eyeZ, cam.centerX, cam.centerY, cam.centerZ, 0, 1, 0)

def on_close():
	pass

def create_menu():
	menu = None
	Glut.glutCreateMenu(menu)
	Glut.glutAddMenuEntry(menu, 1)
	Glut.glutAttachMenu(1)

def init_graphics():
	Gl.glEnable(Gl.GL_LIGHTING)
	Gl.glEnable(Gl.GL_LIGHT0)
	Gl.glLightfv(Gl.GL_LIGHT0, Gl.GL_POSITION, (.2, .2, -5))
	Gl.glEnable(Gl.GL_COLOR_MATERIAL)
	Gl.glClearColor(.3, .1, .3, 1.0)
	Gl.glPolygonMode(Gl.GL_FRONT_AND_BACK, Gl.GL_LINE)
	Gl.glHint(Gl.GL_LINE_SMOOTH_HINT, Gl.GL_NICEST)
	Gl.glLineWidth(1.0)

def on_reshape(w, h):
	win.screenX=w
	win.screenY=h
	#Gl.glLoadIdentity()
	Gl.glMatrixMode(Gl.GL_PROJECTION)
	Gl.glViewport(0, 0, w, h)
	Glu.gluPerspective(45, float(w) / h, .000001, 275)
	Gl.glClear(Gl.GL_COLOR_BUFFER_BIT | Gl.GL_DEPTH_BUFFER_BIT)
	Gl.glMatrixMode(Gl.GL_MODELVIEW)
