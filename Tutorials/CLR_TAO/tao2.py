import sys, time
import clr
clr.AddReferenceToFile("./libs/Tao.OpenGl.dll")
clr.AddReferenceToFile("./libs/Tao.FreeGlut.dll")

import Tao.OpenGl.Gl as Gl
import Tao.OpenGl.Glu as Glu
import Tao.FreeGlut.Glut as Glut

def init_graphics():
	Gl.glEnable(Gl.GL_LIGHTING)
	Gl.glEnable(Gl.GL_LIGHT0)
	Gl.glLightfv(Gl.GL_LIGHT0, Gl.GL_POSITION, (.2, .2, -5))

	Gl.glDisable(Gl.GL_DEPTH_TEST)
	Gl.glDisable(Gl.GL_CULL_FACE)
	Gl.glEnable(Gl.GL_COLOR_MATERIAL)
	Gl.glShadeModel(Gl.GL_SMOOTH);
	Gl.glEnable(Gl.GL_MULTISAMPLE)
	Gl.glEnable(Gl.GL_NORMALIZE)
	Gl.glEnable(Gl.GL_POINT_SMOOTH)
	Gl.glEnable(Gl.GL_LINE_SMOOTH)
	Gl.glEnable(Gl.GL_POLYGON_SMOOTH)
	Gl.glEnable(Gl.GL_POLYGON_OFFSET_FILL)
	Gl.glEnable(Gl.GL_BLEND);
	Gl.glBlendFunc(Gl.GL_SRC_ALPHA, Gl.GL_ONE_MINUS_SRC_ALPHA)
	Gl.glClearColor(.3, .1, .3, 1.0)
	Gl.glPolygonMode(Gl.GL_FRONT_AND_BACK, Gl.GL_FILL)

def on_display():
	Gl.glDrawBuffer(Gl.GL_FRONT)
	Gl.glLineWidth(1.0)
	Gl.glColorMaterial(Gl.GL_FRONT_AND_BACK, Gl.GL_AMBIENT_AND_DIFFUSE)
	Gl.glClear(Gl.GL_COLOR_BUFFER_BIT)

	Gl.glPushMatrix()
	Gl.glBegin(Gl.GL_POLYGON)
	Gl.glEdgeFlag(True)
	Gl.glColor3f( 1.0, 0.2, 0.0)
	Gl.glVertex3f(-1.1, 0.3, 0)
	Gl.glColor3f( 0.2, 1.0, 0.0)
	Gl.glVertex3f(-1.4, -1.3, 0)
	Gl.glColor3f( 0.1, 0.1, 1.0)
	Gl.glVertex3f(-3.2, -0.3, 0)
	Gl.glEnd()
	Gl.glPopMatrix()
	Gl.glFlush()
	Glut.glutSwapBuffers()

	Gl.glDrawBuffer(Gl.GL_BACK)
	Gl.glClear(Gl.GL_DEPTH_BUFFER_BIT)
	Gl.glPushMatrix()
	Gl.glBegin(Gl.GL_POLYGON)
	Gl.glEdgeFlag(True)
	Gl.glColor3f( 0.0, 0.8, 0.0)
	Gl.glVertex3f(1.1, 1.3, 0)
	Gl.glVertex3f(1.4, -1.3, 0)
	Gl.glVertex3f(4.2, -1.3, 0)
	Gl.glEnd()
	Gl.glPopMatrix()
	Gl.glFlush()
	Glut.glutSwapBuffers()

def on_reshape(w, h):
	Gl.glMatrixMode(Gl.GL_PROJECTION)
	Gl.glLoadIdentity()
	Gl.glViewport(0, 0, w, h)
	Glu.gluPerspective(50, float(w) / h, .000001, 100)
	Gl.glClear(Gl.GL_COLOR_BUFFER_BIT | Gl.GL_DEPTH_BUFFER_BIT)
	Gl.glMatrixMode(Gl.GL_MODELVIEW)
	Gl.glLoadIdentity()
	Glu.gluLookAt(0, 0, -5, 0, 0, 0, 0, 1, 0)

def idle():
	time.sleep(0.4)
	#while True:
		#time.sleep(0.1)

def main():
	Glut.glutInit()
	Glut.glutInitDisplayMode(Glut.GLUT_DEPTH | Glut.GLUT_DOUBLE | Glut.GLUT_RGBA)
	Glut.glutInitWindowSize(1200, 600)
	Glut.glutCreateWindow("Tao Example")
	init_graphics()
	Glut.glutDisplayFunc(on_display)
	Glut.glutIdleFunc(idle)
	Glut.glutReshapeFunc(on_reshape)
	Glut.glutMainLoop()

if "__main__" == __name__:
	main()
