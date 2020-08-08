#include <stdio.h>
#include <GL/glew.h>
#include <GL/freeglut.h>
#include <math.h>

static struct Vector3f{
    float x;
    float y;
    float z;
    Vector3f(){}
    Vector3f(float x_, float y_, float z_){
        x = x_;
        y = y_;
        z = z_;
    }
};

GLuint VBO;
GLuint IBO;
const double PI = 3.14159265358979323846;
const double c=PI/180.0;

static void RenderSceneCB()
{
	glClear(GL_COLOR_BUFFER_BIT);
    glEnableVertexAttribArray(0);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);
    glDrawElements(GL_TRIANGLES, 300, GL_UNSIGNED_INT, 0);
	glDisableVertexAttribArray(0);
    glutSwapBuffers();
}


static void InitializeGlutCallbacks() { glutDisplayFunc(RenderSceneCB); }

static void CreateVertexBuffer()
{
    Vector3f Vertices[101];
    Vertices[100] = Vector3f(0.0f, 0.0f, 0.0f);
    float x=0,y=0;
    for(int i=0;i<100;i++){
        x=cos(3.6*c*i)*0.5;
        y=sin(3.6*c*i)*0.5;
        Vertices[i] = Vector3f(x,y, 0.0f);
        printf("%d ) x: %f, y: %f\n",i, x, y);
    }

    glGenBuffers(1, &VBO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(Vertices), Vertices, GL_STATIC_DRAW);
}

static void CreateIndexBuffer()
{
    unsigned int indices[300];
    indices[299] = 0;
    for(int i=0;i<299;i++){
        if(i%3 == 2){
            indices[i] = 101;
        }
        else if(i%3 == 1){
            indices[i] = (i-1)/3 + 1;
        }
        else indices[i] = i/3;
    }
    glGenBuffers(1, &IBO);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, IBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGBA);
    glutInitWindowSize(1024, 768);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Tutorial 02");
    InitializeGlutCallbacks();

    GLenum res = glewInit();
    if (res != GLEW_OK) {
    fprintf(stderr, "Error: '%s'\n", glewGetErrorString(res));
    return 1;
    }

    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
    CreateVertexBuffer();
    CreateIndexBuffer();
    glutMainLoop();

    return 0;
}
