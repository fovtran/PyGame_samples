from Init import *

screen = pygame_init()
other = True

print(glGetString(GL_VERSION))
print(glGetString(GL_EXTENSIONS))

C = -1
print(  glGetIntegerv(GL_MAX_TEXTURE_IMAGE_UNITS, 1))
print(  glGetIntegerv(GL_MAX_TEXTURE_SIZE, 1))
print(  glGetIntegerv(GL_MAX_VARYING_VECTORS, 1))
print(  glGetIntegerv(GL_MAX_VERTEX_ATTRIBS, 1))
print(  glGetIntegerv(GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS,1))
print(  glGetIntegerv(GL_MAX_VERTEX_UNIFORM_VECTORS,1))
print(  glGetIntegerv(GL_MAX_VIEWPORT_DIMS, 1))
print(  glGetIntegerv(GL_NUM_COMPRESSED_TEXTURE_FORMATS,1))
print(  glGetIntegerv(GL_NUM_SHADER_BINARY_FORMATS, 1))
print(  glGetIntegerv(GL_MAX_3D_TEXTURE_SIZE, 1))
print(  glGetIntegerv(GL_MAX_ARRAY_TEXTURE_LAYERS, 1))
print(  glGetIntegerv(GL_MAX_COLOR_ATTACHMENTS, 1))
print(  glGetIntegerv(GL_MAX_COMBINED_UNIFORM_BLOCKS,1))
print(  glGetIntegerv(GL_MAX_DRAW_BUFFERS, 1))
print(  glGetIntegerv(GL_MAX_ELEMENTS_INDICES, 1))
print(  glGetIntegerv(GL_MAX_ELEMENTS_VERTICES, 1))
print(  glGetIntegerv(GL_MAX_FRAGMENT_INPUT_COMPONENTS,1))
print(  glGetIntegerv(GL_MAX_FRAGMENT_UNIFORM_BLOCKS,1))
print(  glGetIntegerv(GL_MAX_FRAGMENT_UNIFORM_COMPONENTS,1))
print(  glGetIntegerv(GL_MAX_PROGRAM_TEXEL_OFFSET, 1))
print(  glGetFloatv(GL_MAX_TEXTURE_LOD_BIAS, 1))
print(  glGetIntegerv(GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS,1))
print(  glGetIntegerv(GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS,1))
print(  glGetIntegerv(GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS,1))
print(  glGetIntegerv(GL_MAX_UNIFORM_BUFFER_BINDINGS,1))
print(  glGetIntegerv(GL_MAX_VARYING_COMPONENTS, 1))
print(  glGetIntegerv(GL_MAX_VERTEX_OUTPUT_COMPONENTS,1))
print(  glGetIntegerv(GL_MAX_VERTEX_UNIFORM_BLOCKS,1))
print(  glGetIntegerv(GL_MAX_VERTEX_UNIFORM_COMPONENTS,1))
print(  glGetIntegerv(GL_MIN_PROGRAM_TEXEL_OFFSET, 1))
print(  glGetIntegerv(GL_NUM_EXTENSIONS, 1))
print(  glGetIntegerv(GL_NUM_PROGRAM_BINARY_FORMATS, 1))
print(  glGetIntegerv(GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT,1))
print(  glGetIntegerv(GL_MAX_SAMPLES, 1))

if other:
    print(  glGetIntegerv(GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS, 1))
    print(  glGetIntegerv(GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS, 1))
    print(  glGetIntegerv(GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT, 1))
    # print(  glGetInteger64v(GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS,1))
    # print(  glGetInteger64v(GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS,1))
    # print(  glGetInteger64v(GL_MAX_ELEMENT_INDEX, 1))
    # print(  glGetInteger64v(GL_MAX_SERVER_WAIT_TIMEOUT, 1))
    # print(  glGetInteger64v(GL_MAX_UNIFORM_BLOCK_SIZE, 0))

pygame.quit()
