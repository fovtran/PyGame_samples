import OpenGL
from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLU import *
import pygame
from pygame.locals import *

import numpy as np

buffer_data = np.array([0, 0, 0, 0])

compute_shader_code = """
#version 430 core
layout(local_size_x = 1, local_size_y = 1) in;

layout(std430, binding=9) buffer data{
    vec4 Data[];
};

void main()
{
    Data[0].x = 1;
    Data[0].y = 2;
    Data[0].z = 3;
    Data[0].w = 4;
}
"""

def setup():
    pygame.init()
    window_width = 1000
    window_height = 800
    display = (window_width, window_height)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    print(glGetString(GL_VERSION))
    test()

    pygame.quit()
    quit()

def test():
    print("Creating shader program")
    compute_shader_program = -1
    shader_program = -1

    compute_shader_program = glCreateShader(GL_COMPUTE_SHADER)
    glShaderSource(compute_shader_program, compute_shader_code)
    glCompileShader(compute_shader_program)
    if glGetShaderiv(compute_shader_program, GL_COMPILE_STATUS) != GL_TRUE:
        raise RuntimeError(glGetShaderInfoLog(compute_shader_program))
    shader_program = glCreateProgram()
    glAttachShader(shader_program, compute_shader_program)
    glLinkProgram(shader_program)
    print(glGetProgramInfoLog(shader_program))

    if shader_program != -1:
        ssbo = -1
        print("Binding buffers")
        glUseProgram(shader_program)
        glGenBuffers(1, ssbo)
        glBindBufferBase(GL_SHADER_STORAGE_BUFFER, 9, ssbo)
        glBindBuffer(GL_SHADER_STORAGE_BUFFER, ssbo)
        glBufferData(GL_SHADER_STORAGE_BUFFER, np.ascontiguousarray(buffer_data, dtype=np.float32), GL_DYNAMIC_READ)

        print("Calling compute")
        glDispatchCompute(1, 1, 1)
        glMemoryBarrier(GL_SHADER_STORAGE_BARRIER_BIT)

        block_index = glGetProgramResourceIndex(shader_program, GL_SHADER_STORAGE_BLOCK, "data", 9)
        if block_index != GL_INVALID_INDEX:
            print("I think I found the data")
        #   How do I access the data here
            result = glMapBuffer(GL_SHADER_STORAGE_BUFFER, GL_READ_ONLY)
            print(result)
            print(buffer_data)
            glUnmapBuffer(GL_SHADER_STORAGE_BUFFER)


setup()
