from Init import *

compute_shader_code = """
#version 440
#extension GL_ARB_compute_shader : enable
#extension GL_ARB_shader_image_load_store : enable

layout (rgba16, binding=0) uniform image2D sourceTex;           //Textures bound to 0 and 1 resp. that are used to
layout (rgba16, binding=1) uniform image2D targetTex;           //acquire texture and save changes made to texture

// layout (local_size_x = 16, local_size_y = 16) in;
out vec4 Data[];
vec3 pxlPos;

void main(){
    vec4 result;
    Data[0].x = 1;
    Data[0].y = 2;
    Data[0].z = 3;
    Data[0].w = 4;
    pxlPos = ivec2(gl_GlobalInvocationID.xz);     //Get pxl-pos
    imageStore(targetTex, pxlPos, vec4(1.0f));    //Write white to texture
}
"""

def setup():
    screen = pygame_init()
    # not work glgetstring -> print(glGetString(GL_VERSION))
    runner()

    pygame.quit()
    quit()

def runner():
    work_grp_size=np.array([0,0,0], dtype=np.int32)
    # glGetIntegeri_v(GL_MAX_COMPUTE_WORK_GROUP_SIZE, 0, work_grp_size[0])
    # glGetIntegeri_v(GL_MAX_COMPUTE_WORK_GROUP_SIZE, 1, work_grp_size[1])
    # glGetIntegeri_v(GL_MAX_COMPUTE_WORK_GROUP_SIZE, 2, work_grp_size[2])
    print("GL_MAX_RENDERBUFFER_SIZE ", glGetInteger(GL_MAX_RENDERBUFFER_SIZE,1))
    print("GL_MAX_UNIFORM_BUFFER_BINDINGS ", glGetInteger(GL_MAX_UNIFORM_BUFFER_BINDINGS,1))
    #print(glGetInteger(GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS,1))
    #print(glGetIntegeri_v(GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS,0))
    print("max local (in one shader) work group sizes x:{0} y:{0} z:{0}", work_grp_size[0], work_grp_size[1], work_grp_size[2]);

    print("Creating shader program")
    shader_program = 1
    ray_shader = 1
    shader_program = glCreateShader(GL_VERTEX_SHADER)
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
        #glBindBufferBase(GL_SHADER_STORAGE_BUFFER, 0, ssbo)
        #glBindBuffer(GL_SHADER_STORAGE_BUFFER, ssbo)
        #glBufferData(GL_SHADER_STORAGE_BUFFER, np.ascontiguousarray(buffer_data, dtype=np.float32), GL_DYNAMIC_READ)

        print("Calling compute")
        if bool(glDispatchCompute):
            print("Calling compute OK")
            # https://registry.khronos.org/OpenGL-Refpages/gl4/html/glDispatchCompute.xhtml
            #glDispatchCompute(1, 1, 1)

        if bool(glMemoryBarrier):
            print("Memory barrier OK")
            glMemoryBarrier(GL_SHADER_STORAGE_BARRIER_BIT)

        block_index = glGetProgramResourceIndex(ray_shader, GL_SHADER_STORAGE_BLOCK, "data", 0)
        if block_index != GL_INVALID_INDEX:
            print("I think I found the data")
            result = glMapBuffer(GL_SHADER_STORAGE_BUFFER, GL_READ_ONLY)
            print(result)
            print(buffer_data)
            glUnmapBuffer(GL_SHADER_STORAGE_BUFFER)

        glDeleteProgram(ray_shader)


setup()
