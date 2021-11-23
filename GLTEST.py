
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT import freeglut
print("Imports successful!") # If you see this printed to the console then installation was successful

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)


OpenGL.GLUT.glutInit # Initialize a glut instance which will allow us to customize our window
if (OpenGL.GLUT.glutInitDisplayMode):
    OpenGL.GLUT.glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
if glutInitWindowSize:
    glutInitWindowSize(500, 500)   # Set the width and height of your window
if glutInitWindowPosition:
    glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
if glutCreateWindow:
    wind = glutCreateWindow("OpenGL Coding Practice") # Give your window a title

if glutDisplayFunc:
    glutDisplayFunc(showScreen())  # Tell OpenGL to call the showScreen method continuously

if glutIdleFunc:
    glutIdleFunc(showScreen)     # Draw any graphics or shapes in the showScreen function at all times
if glutMainLoop:
    glutMainLoop()  # Keeps the window created above displaying/running in a loop

# glmf32.dll
# freeglut.dll
# glu32.dll
# opengl32.dll
