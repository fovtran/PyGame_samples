#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <SDL/SDL.h>
#include <GL/glew.h>

/* dimensions de la fenetre */
#define W 256
#define H 256

void transferToTexture (GLubyte* data, GLuint texID, int width,int height);
void texRGBASpeDisplay(GLuint tex,int width, int height);
void ShutDown(int);
void createTexParam();
void printProgramInfoLog(GLuint obj);
void printShaderInfoLog(GLuint obj);
void checkGLErrors (const char *label);
void initTex(GLuint tex,int width, int height);
GLuint initGLSL(void);

struct struct_textureParameters {
	GLenum texTarget;
	GLenum texInternalFormat;
	GLenum texFormat;
	GLenum dataFormat;
	char* shader_source;
}textureParameters;

int main(void)
{
    int loop = 1;       /* booleen du 'main loop' */
    SDL_Event ev;       /* structure d'evenement(s) SDL */
    GLuint program;     /* notre program */
    GLuint texture;
    GLuint texLoc;

    int use_shaders = 0;/* booleen indiquant si l'on utilise les shaders */
int width = W;
int height = H;
GLuint widthLoc;
GLuint heightLoc;

    /* initialisation de la SDL en mode OpenGL */
    if(SDL_Init(SDL_INIT_VIDEO) < 0)
        exit(EXIT_FAILURE);

    if(SDL_SetVideoMode(width, height, 32, SDL_OPENGL) == NULL)
        ShutDown(EXIT_FAILURE);

    /* nom de la fenetre */
    SDL_WM_SetCaption("GLSL Shaders", NULL);

    /* initialisation de glew */
    glewInit();

    createTexParam();
glEnable( textureParameters.texTarget);
	initTex(texture,width,height);

    /* chargement de notre program */
    program=initGLSL();
    if(program == 0)

        ShutDown(EXIT_FAILURE);
 // Get location of the texture samplers for future use

    GLubyte * data;
    data=(GLubyte*)malloc(width*height*4*sizeof(GLubyte));
    int i;
    for(i=0;i<(width*height*4);i++)
{
	data[i]=100;
}
 transferToTexture (data, texture, width, height);
//texRGBASpeDisplay(texture,width, height);

 glUseProgram(program);
    texLoc = glGetUniformLocation(program, "tex");
    widthLoc = glGetUniformLocation(program, "width");
    heightLoc = glGetUniformLocation(program, "height");
printf("loc : %u",texLoc);
printf("loc : %u",widthLoc);
printf("loc : %u",heightLoc);
glUseProgram(0);

    /* boucle d'affichage principale */
    while(loop)
    {

        /* recuperation d'un evenement */
        SDL_WaitEvent(&ev);

        /* analyse */
        if(ev.type == SDL_QUIT)
            loop = 0;
        else if(ev.type == SDL_KEYDOWN)
            use_shaders = !use_shaders;

        glClear(GL_COLOR_BUFFER_BIT);

        /* on active notre program */
        if(use_shaders)
	{
            glUseProgram(program);
    glActiveTexture(GL_TEXTURE1);
    //glBindTexture(textureParameters.texTarget,texture);
    glUniform1i(texLoc,1);
    glUniform1i(widthLoc,width);
    glUniform1i(heightLoc,height);
    //glBindTexture(textureParameters.texTarget,0);
	}
        /* a partir de la, tous les rendus qui seront effectues seront
           affectes par le program */
        glBindTexture(textureParameters.texTarget,texture);
        glBegin(GL_TRIANGLES);
            glColor3f(1.0, 0.0, 0.0); glVertex2f(0.9, -0.9);
            glColor3f(0.0, 1.0, 0.0); glVertex2f(-0.9, -0.9);
            glColor3f(0.0, 0.0, 1.0); glVertex2f(0.0, 0.9);
        glEnd();

        /* on desactive */
        if(use_shaders)
            glUseProgram(0);

        /* on flip les tampons */
        glFlush();
        SDL_GL_SwapBuffers();
    }
    ShutDown(EXIT_SUCCESS);
    return EXIT_SUCCESS;
}

void createTexParam(){
    textureParameters.texTarget		= GL_TEXTURE_2D;
    textureParameters.texInternalFormat	= GL_RGBA8;
    textureParameters.texFormat		= GL_RGBA;
    textureParameters.dataFormat		= GL_UNSIGNED_BYTE;
    textureParameters.shader_source	= \
//	"#version 130
"
	"uniform int width;" \
	"uniform int height;" \
	"uniform sampler2D tex;" \
	"void main(void) { " \
	//" gl_FragColor = texelFetch(tex, ivec2(2,2),0);"
//"gl_FragColor =  texture2D(tex, gl_TexCoord[0].st);"
"vec2 texCoord;"\
"float temp1;"\
"float temp2;"\
"temp1=gl_FragCoord.x;"\
"texCoord.x = temp1/width;"\
"temp2=gl_FragCoord.y;"\
"texCoord.y = temp2/height;"\
"gl_FragColor =  texture2D(tex, texCoord);"\
//"gl_FragColor =  gl_Color/vec4(texCoord,texCoord);"
	"}";
}

void ShutDown(int code)
{
    SDL_Quit();
    exit(code);
}
void transferToTexture (GLubyte* data, GLuint texID,int width,int height) {
    // version (a): HW-accelerated on NVIDIA
    glBindTexture(textureParameters.texTarget, texID);
    glTexImage2D(textureParameters.texTarget,0,textureParameters.texInternalFormat,width,height,0,textureParameters.texFormat,textureParameters.dataFormat,data);
}
GLuint initGLSL(void) {
    GLuint program;
    GLuint fragmentShader;
    // create program object
    program = glCreateProgram();
    // create shader object (fragment shader)
    fragmentShader = glCreateShader(GL_FRAGMENT_SHADER_ARB);
    // set source for shader
    const GLchar* source = textureParameters.shader_source;
    glShaderSource(fragmentShader, 1, &source, NULL);
    // compile shader
    glCompileShader(fragmentShader);
 // check for errors
    printShaderInfoLog(fragmentShader);
    // attach shader to program
    glAttachShader (program, fragmentShader);
    // link into full program, use fixed function vertex pipeline
    glLinkProgram(program);
 // check for errors
    printProgramInfoLog(program);
    checkGLErrors("render(2)");
    return program;
}

void texRGBASpeDisplay(GLuint tex,int width, int height)
{
		int i;
		GLubyte* data;
		data = malloc(width*height*4*sizeof(GLubyte));
		//printf("BEGIN_RESULTS ONLY_FIRST COLOR %s
",name);
		glBindTexture(textureParameters.texTarget, tex);
		//glReadBuffer(attachmentpoints[readTex]);
		//glCopyTexImage2D(GL_TEXTURE_RECTANGLE_ARB, 0, textureParameters.texInternalFormat, 0,0,texSize,texSize,0);
		glGetTexImage(textureParameters.texTarget, 0,textureParameters.texFormat,textureParameters.dataFormat, data);
printf("DISP
");
		for (i=0; i<(width*height*4); i+=4)
		{
			printf("row =%u :",(i/4)/width);
			printf("column =%u :",(i/4)%width);
			printf("r:%i",data[i]);
			printf("g:%i",data[i+1]);
			printf("b:%i",data[i+2]);
			printf("a:%i
",data[i+3]);
		}
		free(data);
		glBindTexture(textureParameters.texTarget, 0 );
}

void printProgramInfoLog(GLuint obj) {
    int infologLength = 0;
    int charsWritten  = 0;
    char *infoLog;
    glGetProgramiv(obj, GL_INFO_LOG_LENGTH, &infologLength);
    if (infologLength > 1) {
        infoLog = (char *)malloc(infologLength);
        glGetProgramInfoLog(obj, infologLength, &charsWritten, infoLog);
        printf(infoLog);
        printf("
");
        free(infoLog);
    }
}
void printShaderInfoLog(GLuint obj) {
    int infologLength = 0;
    int charsWritten  = 0;
    char *infoLog;
    glGetShaderiv(obj, GL_INFO_LOG_LENGTH, &infologLength);
    if (infologLength > 1) {
        infoLog = (char *)malloc(infologLength);
        glGetShaderInfoLog(obj, infologLength, &charsWritten, infoLog);
        printf(infoLog);
        printf("
");
        free(infoLog);
    }
}

void checkGLErrors (const char *label) {
    GLenum errCode;
    const GLubyte *errStr;

    if ((errCode = glGetError()) != GL_NO_ERROR) {
	errStr = gluErrorString(errCode);
	printf("OpenGL ERROR: ");
	printf((char*)errStr);
	printf("(Label: ");
	printf(label);
	printf(")
.");
    }
}
void initTex(GLuint tex,int width, int height)
{
	glGenTextures(1, &tex);

	glBindTexture(textureParameters.texTarget, tex);
	glTexParameterf(textureParameters.texTarget, GL_TEXTURE_WRAP_S, GL_REPEAT);
	glTexParameterf(textureParameters.texTarget, GL_TEXTURE_WRAP_T, GL_REPEAT);
	glTexParameterf(textureParameters.texTarget, GL_TEXTURE_MAG_FILTER,GL_NEAREST);
	glTexParameterf(textureParameters.texTarget, GL_TEXTURE_MIN_FILTER,GL_NEAREST);
	glTexImage2D(textureParameters.texTarget, 0, textureParameters.texInternalFormat,  W, H, 0, textureParameters.texFormat, textureParameters.dataFormat, NULL);
}
 
