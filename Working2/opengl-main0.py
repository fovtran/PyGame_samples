import OpenGL.GL as GL
import OpenGL.GL.shaders
from OpenGL.GL.ARB.geometry_shader4 import *
from OpenGL.GL.EXT.geometry_shader4 import *
#from OpenGL.GLU import *
#from OpenGL.GLUT import *
import ctypes
import pygame
import numpy

vertex_shader = """
#version 330 core

in vec4 position;

void main()
{
   gl_Position = position;
}
"""

fragment_shader = """
#version 330 core

void main()
{
    // 1- FragColor = texture(texture1, TexCoords);
    gl_FragColor = vec4(1.0f, 1.0f, 0.0f, 0.3f);
}
"""

def square(x,y,z):
    vertices = [ x, y, z, 1.0,
                -x,  y, z, 1.0,
                x, -y, z, 1.0,
                -x, -y, z, 1.0,
                x, -y, z, 1.0,
                -x, y, z, 1.0
                 ]

    vertices = numpy.array(vertices, dtype=numpy.float32) # VBO takes float32. just in case
    return vertices

def triangle(x,y,z):
    vertices = [ x, y, z, 1.0,
                -x,  y, z, 1.0,
                 x, -y, z, 1.0]

    vertices = numpy.array(vertices, dtype=numpy.float32) # VBO takes float32. just in case
    return vertices

def create_object(shader):
    # Create a new VAO (Vertex Array Object) and bind it
    vertex_array_object = GL.glGenVertexArrays(1)
    GL.glBindVertexArray( vertex_array_object )

    # Generate buffers to hold our vertices
    vertex_buffer = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vertex_buffer)

    # Get the position of the 'position' in parameter of our shader and bind it.
    position = GL.glGetAttribLocation(shader, 'position')
    GL.glEnableVertexAttribArray(position)

    # Describe the position data layout in the buffer
    GL.glVertexAttribPointer(position, 4, GL.GL_FLOAT, False, 0, ctypes.c_void_p(0))

    #vertices = triangle(0.6, 0.6, -1.0)
    vertices = square(0.06, 0.06, 0.0)

    # Send the data over to the buffer
    print(GL.GL_FLOAT)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, GL.GL_FLOAT*6, vertices, GL.GL_STATIC_DRAW)

    # Unbind the VAO first (Important)
    GL.glBindVertexArray( 0 )

    # Unbind other stuff
    GL.glDisableVertexAttribArray(position)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
    return vertex_array_object

def display(shader, vertex_array_object):
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    GL.glUseProgram(shader)
    GL.glBindVertexArray( vertex_array_object )
    GL.glDrawArrays(GL.GL_POINTS, 0, 6)
    GL.glDrawArrays(GL.GL_LINES, 0, 6)
    GL.glBindVertexArray( 0 )
    GL.glUseProgram(0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((512, 512), pygame.OPENGL|pygame.DOUBLEBUF)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glHint(GL.GL_PERSPECTIVE_CORRECTION_HINT, GL.GL_NICEST)
    GL.glEnable(GL.GL_POINT_SMOOTH)
    GL.glEnable(GL.GL_LINE_SMOOTH)
    #GL.glEnable(GL.GL_BLEND)
    #GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
    # - It is also possible to set different options for the RGB and alpha channel individually using glBlendFuncSeparate:
    # glBlendFuncSeparate(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_ONE, GL_ZERO);

    GL.glClearColor(0.0, 0.0, 0.1, 1.0)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GL.glMatrixMode(GL.GL_MODELVIEW)

    shader = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(vertex_shader, GL.GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(fragment_shader, GL.GL_FRAGMENT_SHADER)
    )

    vertex_array_object = create_object(shader)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                return

        display(shader, vertex_array_object)
        pygame.display.flip()

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
