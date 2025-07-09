# import importlib
from OpenGL.GL import glMatrixMode, glLoadIdentity, glOrtho, GL_MODELVIEW, GL_PROJECTION
from OpenGL.GLU import gluPerspective, gluLookAt

w = 0 
h = 0

class Perspective:
    def __init__(self, _w, _h):
        self.setviewport(_w, _h)

    def setviewport(self, _w, _h):
        global w, h
        w = _w
        h = _h

    def lookAt(self):
        # Front view
        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
        # Reaer view,
        #gluLookAt(0, 0, -10, 0, 0, 0, 0, 1, 0)

    def LD_I(self):
        print("Identity matrix")
        # store current matrix
        glMatrixMode( GL_PROJECTION );
        glLoadIdentity();
        # restore current matrix
        glMatrixMode( GL_MODELVIEW ); # Defailt Identity matches monitor not viewpoert,

    def LD_DEF(self):
        print("DEF perspective")
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, float(w) / h, .0001, 1000) # Minimum DOF is 0.0001
        self.lookAt()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def LD_2D(self):
        print("2D perspective")
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        #glOrtho(0, w,0, h, 0.001, 1000)
        gluPerspective(5.0, float(w)/float(h), .0001, 1000)
        self.lookAt()
        glMatrixMode(GL_MODELVIEW)

    def LD_3D(self):
        print("3D perspective")
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(15.0, float(w)/float(h), 0.0001, 1000)
        self.lookAt()
        glMatrixMode(GL_MODELVIEW)

    def LD_4D(self):
        print("4D perspective")
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, float(w) / h, .0001, 1000)
        self.lookAt()
        glMatrixMode(GL_MODELVIEW)
