import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL.ARB.geometry_shader4 import *
from OpenGL.GL.EXT.geometry_shader4 import *

import PIL
import numpy
import numpy.linalg as linalg
import random
from math import sin, cos

shader = None
USE_POINTS = False

def display(clock, shader):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    t = clock
    rot = t % (10*1000)
    theta = 2 * 3.141592 * (rot / 10000.0)

    glLoadIdentity()
    gluLookAt(-10*sin(theta), -10*cos(theta),   0,
                0,   0,   0,
                0,   0,   1)

    glUseProgram(shader)
    glUniform1f(glGetUniformLocation(shader, "distance"), rot/10000.0)

    # difference #1
    glBegin(GL_POINTS if USE_POINTS else GL_LINES)
    for x in [-2.5, 0, 2.5]:
        for y in [-2.5, 0, 2.5]:
            glVertexAttrib1f(7, random.uniform(0.0, 1.0))
            glVertexAttrib3f(0, x, y, 0)
            # difference #2
            if not USE_POINTS:
                glVertexAttrib1f(7, random.uniform(0.0, 1.0))
                glVertexAttrib3f(0, x, y, 0)
    #glEnd()
    glUseProgram(0)
    pygame.display.flip()

def reshape(width, height):
    aspect = float(width)/float(height) if (height>0) else 1.0
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45.0,
                   aspect,
                   1.0, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode((512, 512), pygame.OPENGL|pygame.DOUBLEBUF)
glEnable(GL_DEPTH_TEST)
glEnable(GL_POINT_SMOOTH)
glEnable(GL_LINE_SMOOTH)
reshape(512,512)

shader = glCreateProgram()
vertex_shader = glCreateShader(GL_VERTEX_SHADER)
geometry_shader = glCreateShader(GL_GEOMETRY_SHADER)
fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)

# difference #3
glProgramParameteriEXT(shader, GL_GEOMETRY_INPUT_TYPE_ARB, GL_POINTS if USE_POINTS else GL_LINES)
glProgramParameteriEXT(shader, GL_GEOMETRY_OUTPUT_TYPE_ARB, GL_LINE_STRIP)
glProgramParameteriEXT(shader, GL_GEOMETRY_VERTICES_OUT_ARB, 100)

glAttachShader(shader, vertex_shader)
glAttachShader(shader, geometry_shader)
glAttachShader(shader, fragment_shader)

glShaderSource(vertex_shader, """
attribute float color;
varying float geom_color;
// in ivec4 vertex;
// out ivec4 v;

void main(void) {
  gl_Position = gl_Vertex;
  geom_color = color;
}
""")
glCompileShader(vertex_shader)
print (glGetShaderInfoLog(vertex_shader))

glShaderSource(geometry_shader, """
#version 120
#extension GL_EXT_geometry_shader4 : enable

varying in float geom_color[1];
varying out float frag_color;
// in ivec4 v[gl_VerticesIn];

uniform float distance;

void main(void)
{
 int x, y;

 for(x=-1; x<=1; x+=1) {
   for(y=-1; y<=1; y+=1) {
    //StartPrimitive(); // FIX FIX FIX
     gl_Position = gl_PositionIn[0];
     gl_Position.x += x * distance;
     gl_Position.y += y * distance;
     gl_Position.z -= 2.0;
     gl_Position = gl_ModelViewProjectionMatrix * gl_Position;
     frag_color = geom_color[0];
     EmitVertex();

     gl_Position = gl_PositionIn[0];
     gl_Position.x += x * distance;
     gl_Position.y += y * distance;
     gl_Position.z += 2.0;
     gl_Position = gl_ModelViewProjectionMatrix * gl_Position;
     frag_color = geom_color[0];
     EmitVertex();
     //EndPrimitive();
   }
 }
}
""")
glCompileShader(geometry_shader)
print (glGetShaderInfoLog(geometry_shader))

glShaderSource(fragment_shader, """
varying float frag_color;
void main(void) {
  gl_FragColor = vec4(frag_color,1.0-frag_color,frag_color,1);
}
""")
glCompileShader(fragment_shader)
print (glGetShaderInfoLog(fragment_shader))

glLinkProgram(shader)
print (glGetProgramInfoLog(shader))

glBindAttribLocation(shader, 7, "color")

glLinkProgram(shader)
print (glGetProgramInfoLog(shader))

clock = pygame.time.Clock()

def Controls():
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          exit()
      if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
          exit()

while True:
    Controls()
    clock = pygame.time.get_ticks()
    display(clock, shader)
    pygame.display.flip()
    pygame.time.wait(25)
