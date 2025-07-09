#version 430

// Define the layout of the compute shader's work group
layout (local_size_x = 16, local_size_y = 16) in;

// Bind the input/output image
layout (rgba32f, binding = 0) uniform image2D img;

void main() {
    // Get the current work group coordinates
    ivec2 pixel_coords = ivec2(gl_GlobalInvocationID.xy);

    // Read the current pixel color
    vec4 pixel = imageLoad(img, pixel_coords);

    // Apply a simple effect (e.g., invert colors)
    vec4 inverted_pixel = vec4(1.0 - pixel.rgb, pixel.a);

    // Write the modified pixel back to the image
    imageStore(img, pixel_coords, inverted_pixel);
}

#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <iostream>

// Function to create and compile a compute shader
GLuint createComputeShader(const char* source) {
    GLuint shader = glCreateShader(GL_COMPUTE_SHADER);
    glShaderSource(shader, 1, &source, nullptr);
    glCompileShader(shader);

    // Check for compilation errors
    GLint success;
    glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
    if (!success) {
        char infoLog[512];
        glGetShaderInfoLog(shader, 512, nullptr, infoLog);
        std::cerr << "ERROR::COMPUTE_SHADER::COMPILATION_FAILED\n" << infoLog << std::endl;
    }

    return shader;
}

int main() {
    // Initialize GLFW and create a window
    if (!glfwInit()) return -1;
    GLFWwindow* window = glfwCreateWindow(800, 600, "Compute Shader Example", nullptr, nullptr);
    if (!window) {
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    glewInit();

    // Define the compute shader source
    const char* computeShaderSource = R"(
        #version 430
        layout (local_size_x = 16, local_size_y = 16) in;
        layout (rgba32f, binding = 0) uniform image2D img;
        void main() {
            ivec2 pixel_coords = ivec2(gl_GlobalInvocationID.xy);
            vec4 pixel = imageLoad(img, pixel_coords);
            vec4 inverted_pixel = vec4(1.0 - pixel.rgb, pixel.a);
            imageStore(img, pixel_coords, inverted_pixel);
        }
    )";

    // Create and link the compute shader program
    GLuint computeShader = createComputeShader(computeShaderSource);
    GLuint computeProgram = glCreateProgram();
    glAttachShader(computeProgram, computeShader);
    glLinkProgram(computeProgram);

    // Check for linking errors
    GLint success;
    glGetProgramiv(computeProgram, GL_LINK_STATUS, &success);
    if (!success) {
        char infoLog[512];
        glGetProgramInfoLog(computeProgram, 512, nullptr, infoLog);
        std::cerr << "ERROR::PROGRAM::LINKING_FAILED\n" << infoLog << std::endl;
    }

    // Bind a texture to be processed by the compute shader
    GLuint texture;
    glGenTextures(1, &texture);
    glBindTexture(GL_TEXTURE_2D, texture);
    glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGBA32F, 512, 512);

    // Bind the texture to image unit 0
    glBindImageTexture(0, texture, 0, GL_FALSE, 0, GL_READ_WRITE, GL_RGBA32F);

    // Use the compute shader program
    glUseProgram(computeProgram);

    // Dispatch compute work groups
    glDispatchCompute(512 / 16, 512 / 16, 1);

    // Ensure all compute operations are complete
    glMemoryBarrier(GL_SHADER_IMAGE_ACCESS_BARRIER_BIT);

    // Main loop (for demonstration purposes)
    while (!glfwWindowShouldClose(window)) {
        glClear(GL_COLOR_BUFFER_BIT);
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    // Cleanup
    glDeleteProgram(computeProgram);
    glDeleteShader(computeShader);
    glDeleteTextures(1, &texture);
    glfwDestroyWindow(window);
    glfwTerminate();

    return 0;
}
