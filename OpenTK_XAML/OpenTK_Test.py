import clr
clr.AddReferenceToFileAndPath("./.NuGet/packages/OpenTK.3.2/lib/net20/OpenTK.dll")

from System import UInt32, IntPtr
from ctypes import *

import OpenTK
from OpenTK.Graphics import *
from OpenTK.Graphics.OpenGL import GL
from OpenTK.Graphics.ES20 import ClearBufferMask
from OpenTK.Input import Keyboard, Key

from math import cos,sin,pi
from NP import *

def init_graphics():
	Enable(Gl.GL_LIGHTING)
	Enable(Gl.GL_LIGHT0)
	Lightfv(Gl.GL_LIGHT0, Gl.GL_POSITION, (.2, .2, -5))
	Enable(Gl.GL_COLOR_MATERIAL)
	ClearColor(.3, .1, .3, 1.0)
	PolygonMode(Gl.GL_FRONT_AND_BACK, Gl.GL_LINE)
	Hint(Gl.GL_LINE_SMOOTH_HINT, Gl.GL_NICEST)

def on_display():
	#Gl.glColorMaterial(Gl.GL_FRONT, Gl.GL_DIFFUSE)
	#Gl.GL.Clear(ClearBufferMask.ColorBufferBit)

	A = linspace(0, 2*pi, 4)
	for z in linspace(1, 10, 5):
		for v in A:
			Gl.GL.glTranslatef(cos(v), sin(v), z)

	GL.glClear(Gl.GL_DEPTH_BUFFER_BIT)
	GL.glFlush()

def on_reshape(w, h):
	GL.MatrixMode(GL_PROJECTION)
	LoadIdentity()
	Viewport(0, 0, w, h)
	#Glu.gluPerspective(50, float(w) / h, .000001, 10)
	#Gl.GL.glClear(Gl.GL_COLOR_BUFFER_BIT | Gl.GL_DEPTH_BUFFER_BIT)
	MatrixMode(Gl.GL_MODELVIEW)
	LoadIdentity()

def main():
	OpenTK.GameWindow(800,600)
	on_reshape(800,600)
	on_display()

if "__main__" == __name__:
	main()
