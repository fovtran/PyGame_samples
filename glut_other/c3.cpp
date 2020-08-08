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

void render(void);
void keyboard(int key, int x, int y);

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
    glutInitWindowPosition(100, 100); //Position of the window
    glutInitWindowSize(620, 440); //Screen Size
    glClearColor (0.0, 1.0, 0.0, 0.0 );
    glutCreateWindow("Greeting Card");  //Creates the window and names it

    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA); // Enables Alpha channel
    glutDisplayFunc(render);
    glutDisplayFunc(draw);
    glutKeyboardFunc(keyboard);
    glutMainLoop();   //Finished, now render
    }

void keyboard (unsigned char key, int x, int y)
{
    GLfloat colors[][3] = { { 0.0f, 0.0f, 1.0f}, {1.0f, 0.0f, 0.0f } };
    static int back;

    switch (key) {
    case 27:
        exit(0);
    default:
        back ^= 1;
        glClearColor(colors[back][0], colors[back][1], colors[back][2], 1.0f);
        glutPostRedisplay();
    }
}

void render(void) {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);


    // World Snow //
    glPushMatrix();
    glTranslatef(0, -0.35, 0);   //Position of the shape

        glBegin(GL_POLYGON);  //Defines the type of shape
        glColor3f(1, 1,1);    //Colour of the shape 'RED, GREEN, BLUE'
        glVertex2f(-1.5,-0.7); //Vertex 2F  Gives the vertex some coords

        glColor3f(1, 1, 1);
        glVertex2f(-1.5, 0.7);

        glColor3f(1, 1, 1);
        glVertex2f( 1.5, 0.7);

        glColor3f(1, 1, 1);
        glVertex2f( 1.5,-0.7);
        glEnd();
        glPopMatrix();
        glFlush();

    // Grey gradient world
        glPushMatrix();
    glTranslatef(0, -0.35, 0);

        glBegin(GL_POLYGON);
        glColor3f(1, 1, 1);
        glVertex2f(-1.5,-0.7);

        glColor3f(1, 1, 1);
        glVertex2f(-1.5, 0.7);

        glColor3f(0.658824, 0.658824, 0.658824);
        glVertex2f( 1.5, 0.7);

        glColor3f(1, 1, 1);
        glVertex2f( 1.5,-1.7);
        glEnd();
        glPopMatrix();
        glFlush();


    // Top of the first Tree //
    glPushMatrix();
    glTranslatef(-0.6, 0.5, 0);
    glBegin(GL_TRIANGLES);  //Defines the shape as being a triangle


        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(-0.1, -0.1);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.1, -0.1);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.0, 0.1);
            glEnd();
        glPopMatrix();


 // Middle of the first tree


    glPushMatrix();
    glTranslatef(-0.6, 0.4, 0);
    glBegin(GL_TRIANGLES);
        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(-0.1, -0.1);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.1, -0.1);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.0, 0.1);

    glEnd();
    glPopMatrix();


    // Bottom of the first tree

    glPushMatrix();
    glTranslatef(-0.6, 0.3, 0);
    glBegin(GL_TRIANGLES);
        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(-0.1, -0.1);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.1, -0.1);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.0, 0.1);

    glEnd();
    glPopMatrix();
    glFlush();


    //Stump of first tree

    glPushMatrix();
    glTranslatef(-0.6, 0.16, 0);

    glBegin(GL_POLYGON);
        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f(-0.02,-0.04);

        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f(-0.02, 0.04);

        glColor3f( 0.647059, 0.164706, 0.164706);
        glVertex2f( 0.02, 0.04);

        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f( 0.02,-0.04);


    glEnd();
    glPopMatrix();

    // Large Tree TOP
        glPushMatrix();
    glTranslatef(-0.2, 0, 0);
    glBegin(GL_TRIANGLES);
        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(-0.15, -0.15);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.15, -0.15);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.0, 0.15);

    glEnd();
    glPopMatrix();
    glFlush();

    //Large Tree MIDDLE
    glPushMatrix();
    glTranslatef(-0.2, -0.15, 0);
    glBegin(GL_TRIANGLES);
        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(-0.15, -0.15);

        glColor3f( 0.137255, 0.556863,0.137255);;
        glVertex2f(0.15, -0.15);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.0, 0.15);

    glEnd();
    glPopMatrix();
    glFlush();

    //Large Tree Bottom
    glPushMatrix();
    glTranslatef(-0.2, -0.30, 0);
    glBegin(GL_TRIANGLES);
        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(-0.15, -0.15);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.15, -0.15);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.0, 0.15);

    glEnd();
    glPopMatrix();
    glFlush();

    //Smaller tree Top
    glPushMatrix();
    glTranslatef(0.05, 0.45, 0);
    glBegin(GL_TRIANGLES);
        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(-0.05, -0.05);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.05, -0.05);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.0, 0.05);

    glEnd();
    glPopMatrix();
    glFlush();

    //Smaller tree MIDDLE
    glPushMatrix();
    glTranslatef(0.05, 0.40, 0);
    glBegin(GL_TRIANGLES);
        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(-0.05, -0.05);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.05, -0.05);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.0, 0.05);

    glEnd();
    glPopMatrix();
    glFlush();

    //smaller tree bottom
        glPushMatrix();
    glTranslatef(0.05, 0.50, 0);
    glBegin(GL_TRIANGLES);
        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(-0.05, -0.05);

        glColor3f( 0.137255, 0.556863,0.137255);
        glVertex2f(0.05, -0.05);

        glColor3f(0.32, 0.49, 0.46);
        glVertex2f(0.0, 0.05);

    glEnd();
    glPopMatrix();
    glFlush();

    //Stump of smaller tree
    glPushMatrix();
    glTranslatef(0.05, 0.32, 0);
        glBegin(GL_POLYGON);
        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f(-0.01,-0.03);

        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f(-0.01, 0.03);

        glColor3f( 0.647059, 0.164706, 0.164706);
        glVertex2f( 0.01, 0.03);

        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f( 0.01,-0.03);

        glEnd();
    glPopMatrix();

    //Stump of MAIN tree

        glPushMatrix();
    glTranslatef(-0.2, -0.50, 0);
        glBegin(GL_POLYGON);
        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f(-0.02,-0.05);

        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f(-0.02, 0.05);

        glColor3f( 0.647059, 0.164706, 0.164706);
        glVertex2f( 0.02, 0.05);

        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f( 0.02,-0.05);

        glEnd();
    glPopMatrix();

    // Red Present
    glPushMatrix();
    glTranslatef(0, -0.5, 0);
        glBegin(GL_POLYGON);

        glColor3f( 1, 0, 1);
        glVertex2f(-0.04,-0.05);

        glColor3f( 1, 0, 0);
        glVertex2f(-0.04, 0.05);

        glColor3f( 1, 0, 0);
        glVertex2f( 0.04, 0.05);

        glColor3f( 1, 0, 0);
        glVertex2f( 0.04,-0.05);
        glEnd();
    glPopMatrix();

    //Blue Present
    glPushMatrix();
    glTranslatef(-0.2, -0.7, 0);
        glBegin(GL_POLYGON);

        glColor3f( 0, 0, 1);
        glVertex2f(-0.07,-0.06);

        glColor3f( 0, 0, 1);
        glVertex2f(-0.07, 0.06);

        glColor3f( 0, 0, 1);
        glVertex2f( 0.07, 0.06);

        glColor3f( 0.196078, 0.6, 0.8);
        glVertex2f( 0.07,-0.06);
        glEnd();
    glPopMatrix();


    // BLUE Ribbon RED present VERT
        glPushMatrix();
    glTranslatef(0, -0.5, 0);
        glBegin(GL_POLYGON);

        glColor3f( 0, 0, 1);
        glVertex2f(-0.04,-0.01);

        glColor3f( 0, 0, 1);
        glVertex2f(-0.04, 0.01);

        glColor3f( 0, 0, 1);
        glVertex2f( 0.04, 0.01);

        glColor3f( 0, 0, 1);
        glVertex2f( 0.04,-0.01);
        glEnd();
        glPopMatrix();

        //BLUE ribbon RED present HORIZ
        glPushMatrix();
    glTranslatef(0, -0.5, 0);
        glBegin(GL_POLYGON);

        glColor3f( 0, 0, 1);
        glVertex2f(-0.01,-0.05);

        glColor3f( 0, 0, 1);
        glVertex2f(-0.01, 0.05);

        glColor3f( 0, 0, 1);
        glVertex2f( 0.01, 0.05);

        glColor3f( 0, 0, 1);
        glVertex2f( 0.01,-0.05);
        glEnd();
        glPopMatrix();

        //Yellow Ribbon Blue Present VERT
        glPushMatrix();
    glTranslatef(-0.2, -0.7, 0);
        glBegin(GL_POLYGON);

        glColor3f( 0.6, 0.8, 0.196078);
        glVertex2f(-0.07,-0.01);

        glColor3f( 0.6, 0.8, 0.196078);
        glVertex2f(-0.07, 0.01);

        glColor3f( 0.6, 0.8, 0.196078);
        glVertex2f( 0.07, 0.01);

        glColor3f( 0.6, 0.8, 0.196078);
        glVertex2f( 0.07,-0.01);
        glEnd();
        glPopMatrix();


        // BLUE present YELLOW ribbon VERT
            glPushMatrix();
    glTranslatef(-0.2, -0.7, 0);
        glBegin(GL_POLYGON);

        glColor3f( 0.6, 0.8, 0.196078);
        glVertex2f(-0.01,-0.06);

        glColor3f( 0.6, 0.8, 0.196078);
        glVertex2f(-0.01, 0.06);

        glColor3f( 0.6, 0.8, 0.196078);
        glVertex2f( 0.01, 0.06);

        glColor3f( 0.6, 0.8, 0.196078);
        glVertex2f( 0.01,-0.06);
        glEnd();
        glPopMatrix();


        //Sign Post
    glPushMatrix();
    glTranslatef(0.5, -0.1, 0);
        glBegin(GL_POLYGON);
        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f(-0.02,-0.25);

        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f(-0.02, 0.25);

        glColor3f( 0.35, 0.16, 0.14);
        glVertex2f( 0.02, 0.25);

        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f( 0.02,-0.25);
        glEnd();
        glPopMatrix();


        //Sign, Attatched to the post
    glPushMatrix();
    glTranslatef(0.5, -0.001, 0);
        glBegin(GL_POLYGON);
        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f(-0.15,-0.10);

        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f(-0.15, 0.10);

        glColor3f( 0.35, 0.16, 0.14);
        glVertex2f( 0.15, 0.10);

        glColor3f( 0.36, 0.25, 0.20);
        glVertex2f( 0.15,-0.10);
        glEnd();
        glPopMatrix();

    //Moon
    glPushMatrix();
    glTranslatef(-0.9, 0.90, 0);
    glBegin(GL_POLYGON);
        glColor4f( 0.90, 0.91, 0.98, 1);  //RGBA
        glVertex2f(-0.10,-0.2);

        glColor4f( 0.329412, 0.329412, 0.329412, 1);
        glVertex2f(-0.10, 0.2);

        glColor4f( 0.90, 0.91, 0.98, 1);
        glVertex2f( 0.10, 0.2);
        glColor4f( 0.90, 0.91, 0.98, 1);
        glVertex2f( 0.10,-0.2);
    glEnd();
    glPopMatrix();

    //MAIN PRESENT UNDER SIGN
    glPushMatrix();
    glTranslatef(0.5, -0.6, 0);
        glBegin(GL_POLYGON);

        glColor3f( 0.89, 0.47, 0.20);
        glVertex2f(-0.20,-0.20);

        glColor3f( 0.89, 0.47, 0.20);
        glVertex2f(-0.20, 0.20);

        glColor3f( 0.89, 0.47, 0.20);
        glVertex2f( 0.20, 0.20);

        glColor3f( 1.0, 0.25, 0);
        glVertex2f( 0.20,-0.20);
        glEnd();
    glPopMatrix();

    //Orange Present Purple Ribbon VERT
            glPushMatrix();
    glTranslatef(0.5, -0.6, 0);
        glBegin(GL_POLYGON);

        glColor3f( 0.73, 0.16, 0.96);
        glVertex2f(-0.20,-0.06);

        glColor3f( 0.73, 0.16, 0.96);
        glVertex2f(-0.20, 0.06);

        glColor3f( 0.87, 0.58, 0.98);
        glVertex2f( 0.20, 0.06);

        glColor3f( 0.87, 0.58, 0.98);
        glVertex2f( 0.20,-0.06);
        glEnd();
        glPopMatrix();


        //Orange Present Purple Ribbon HORIZ
        glTranslatef(0.5, -0.6, 0);
        glBegin(GL_POLYGON);

        glColor3f( 0.87, 0.58, 0.98);
        glVertex2f(-0.06,-0.20);

        glColor3f( 0.87, 0.58, 0.98);
        glVertex2f(-0.06, 0.20);

        glColor3f( 0.73, 0.16, 0.96);
        glVertex2f( 0.06, 0.20);

        glColor3f( 0.73, 0.16, 0.96);
        glVertex2f( 0.06,-0.20);
        glEnd();
        glPopMatrix();
        glFlush();


        //'North Pole' TEXT sign
    glPushMatrix();
    glLoadIdentity();
    glTranslatef(0.360, -0.010, 0);
    glRotatef(90,0.0f,0.0f,0.0f);
    glColor3f( 0.0, 0.0, 0.0 ); //Colour is black
    glRasterPos3i(10,100,1);

    char text[50]="North Pole";   //Text

    for(int i=0; i<50; i++)

    {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18,(int)text[i]);
    }
    glPopMatrix();

            glutSwapBuffers();
}
