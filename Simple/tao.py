# Copyright (c) 2013 Ashwin Nanjappa
import sys
#sys.path.append(r"./LIBS")
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
    Gl.glEnable(Gl.GL_DEPTH_TEST)
    Gl.glClearColor(1, 1, 1, 1)

def on_display():
    Gl.glClear(Gl.GL_COLOR_BUFFER_BIT | Gl.GL_DEPTH_BUFFER_BIT)
    Gl.glLoadIdentity()
    Glu.gluLookAt(0, 0, 5, 0, 0, 1, 0, 1, 0)
    Glut.glutSolidTeapot(1)
    Glut.glutSwapBuffers()

def on_reshape(w, h):
    Gl.glMatrixMode(Gl.GL_PROJECTION)
    Gl.glLoadIdentity()
    Gl.glViewport(0, 0, w, h)
    Glu.gluPerspective(40, float(w) / h, 1, 100)
    Gl.glMatrixMode(Gl.GL_MODELVIEW)

def main():
    Glut.glutInit()
    Glut.glutInitWindowSize(500, 500)
    Glut.glutCreateWindow("Tao Example")
    init_graphics()
    Glut.glutDisplayFunc(on_display)
    Glut.glutReshapeFunc(on_reshape)
    Glut.glutMainLoop()

if "__main__" == __name__:
    main()
