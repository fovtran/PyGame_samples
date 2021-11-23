import OpenGL
from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import numpy as np

compute_shader_code = """
#version 330
layout(local_size_x = 1, local_size_y = 1) in;
layout(std430, binding=0) buffer data{  vec4 Data[]; };

void main(){
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
    work_grp_size=[-1,-1,-1];

    #glGetIntegeri_v(GL_MAX_COMPUTE_WORK_GROUP_SIZE, 0, work_grp_size[0]);
    #glGetIntegeri_v(GL_MAX_COMPUTE_WORK_GROUP_SIZE, 1, work_grp_size[1]);
    #glGetIntegeri_v(GL_MAX_COMPUTE_WORK_GROUP_SIZE, 2, work_grp_size[2]);
    print(glGetInteger(GL_MAX_RENDERBUFFER_SIZE,1))
    #print(glGetInteger(GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS,1))
    #print(glGetIntegerv(GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS,1))
    print(glGetInteger(GL_MAX_UNIFORM_BUFFER_BINDINGS,1))

    #print("max local (in one shader) work group sizes x:{0} y:{0} z:{0}", \
    #    work_grp_size[0], work_grp_size[1], work_grp_size[2]);

    print("Creating shader program")
    shader_program = -1
    ray_shader = -1
    # GL_COMPUTE_SHADER = compute_shader_code
    shader_program = glCreateShader(GL_COMPUTE_SHADER)
    glShaderSource(shader_program, compute_shader_code)
    glCompileShader(shader_program)
    if glGetShaderiv(shader_program, GL_COMPILE_STATUS) != GL_TRUE:
        raise RuntimeError(glGetShaderInfoLog(shader_program))
    ray_shader = glCreateProgram()
    glAttachShader(ray_shader, shader_program)
    glLinkProgram(ray_shader)
    print(glGetProgramInfoLog(ray_shader))

    if ray_shader != -1:
        ssbo = -1
        buffer_data = np.array([1, 0, 1, 0])

        print("Binding buffers")
        glUseProgram(ray_shader)
        glGenBuffers(0, ssbo)
        glBindBufferBase(GL_SHADER_STORAGE_BUFFER, 0, ssbo)
        glBindBuffer(GL_SHADER_STORAGE_BUFFER, ssbo)
        glBufferData(GL_SHADER_STORAGE_BUFFER, np.ascontiguousarray(buffer_data, dtype=np.float32), GL_DYNAMIC_READ)

        #print("Calling compute")
        #glDispatchCompute(0)
        #glMemoryBarrier(GL_SHADER_STORAGE_BARRIER_BIT)

        block_index = glGetProgramResourceIndex(ray_shader, GL_SHADER_STORAGE_BLOCK, "data", 0)
        if block_index != GL_INVALID_INDEX:
            print("I think I found the data")
            result = glMapBuffer(GL_SHADER_STORAGE_BUFFER, GL_READ_ONLY)
            print(result)
            print(buffer_data)
            glUnmapBuffer(GL_SHADER_STORAGE_BUFFER)

        glDeleteProgram(ray_shader)


setup()
