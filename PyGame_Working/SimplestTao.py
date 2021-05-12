import sys
import clr
clr.AddReferenceToFile("./libs/Tao.OpenGl.dll")
clr.AddReferenceToFile("./libs/Tao.FreeGlut.dll")

import Tao.OpenGl.Gl as Gl
import Tao.OpenGl.Glu as Glu
import Tao.FreeGlut.Glut as Glut

def init_graphics():
    Gl.glEnable(Gl.GL_LIGHTING)
    Gl.glEnable(Gl.GL_LIGHT0)
    Gl.glLightfv(Gl.GL_LIGHT0, Gl.GL_POSITION, (1, .5, 1))
    Gl.glClearColor(1, 1, 1, 1)

def on_display():
    Gl.glClear(Gl.GL_COLOR_BUFFER_BIT | Gl.GL_DEPTH_BUFFER_BIT)
    Glut.glutSwapBuffers()

def on_reshape(w, h):
	pass 

def main():
    Glut.glutInit()
    Glut.glutMainLoop()

if "__main__" == __name__:
    main()
