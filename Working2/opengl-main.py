from Init import *

vertex_shader = """
#version 330

in vec4 position;
void main()
{
   gl_Position = position;
}
"""

fragment_shader = """
#version 330

void main()
{
   gl_FragColor = vec4(1.0f, 1.0f, 0.0f, 1.0f);
}
"""

vertices = [ 0.6,  0.6, 0.0, 1.0,
            -0.6,  0.6, 0.0, 1.0,
             0.0, -0.6, 0.0, 1.0]

vertices = np.array(vertices, dtype=np.float32)

def create_object(shader):
    # Create a new VAO (Vertex Array Object) and bind it
    vertex_array_object = glGenVertexArrays(1)
    glBindVertexArray( vertex_array_object )

    # Generate buffers to hold our vertices
    vertex_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)

    # Get the position of the 'position' in parameter of our shader and bind it.
    position = glGetAttribLocation(shader, 'position')
    glEnableVertexAttribArray(position)

    # Describe the position data layout in the buffer
    glVertexAttribPointer(position, 4, GL_FLOAT, False, 0, ctypes.c_void_p(0))

    # Send the data over to the buffer
    glBufferData(GL_ARRAY_BUFFER, 48, vertices, GL_STATIC_DRAW)

    # Unbind the VAO first (Important), and unbind other stuff
    glBindVertexArray( 0 )
    glDisableVertexAttribArray(position)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    return vertex_array_object

def display(shader, vertex_array_object):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(shader)

    glBindVertexArray( vertex_array_object )
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray( 0 )

    glUseProgram(0)

def Controls():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return
        
def main():
    screen = pygame_init()

    shader = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    )

    vertex_array_object = create_object(shader)

    clock = pygame.time.Clock()
    while True:
        display(shader, vertex_array_object)
        clock = pygame.time.get_ticks()
        pygame.display.flip()
        Controls()
        pygame.time.wait(25)

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
