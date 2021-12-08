from AllImports import *
from Init import *

def VBO():
	glEnableClientState (GL_VERTEX_ARRAY)
	vertices = [ 0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 1.0, 0.0 ]
	vbo = glGenBuffers (1)
	glBindBuffer (GL_ARRAY_BUFFER, vbo)
	glBufferData (GL_ARRAY_BUFFER, len(vertices)*4, (c_float*len(vertices))(*vertices), GL_STATIC_DRAW)
	glVertexPointer (3, GL_FLOAT, 0, None)

def draw():
	glEnableClientState (GL_VERTEX_ARRAY)
	glColor (0.05, 0.95, 0.05, 1.0)
	glDrawArrays (GL_TRIANGLES, 0, 3)
	glDisableClientState (GL_VERTEX_ARRAY)

running = True
screen = pygame_init()
color_dark = (2,2,2,255)
global LD
LD = glGenLists(4)
LD_CL=LD+4

def lookAt():
	gluLookAt(0,0,-15, 0,0,0, 0, 1, 0)
	pass

VBO()
glNewList(LD, GL_COMPILE)
draw()
glEndList()

glNewList(LD_CL, GL_COMPILE)
draw()
glEndList()

def LD_2D():
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0,w,0,h, 0.1, 1000)
	lookAt()
	glMatrixMode(GL_MODELVIEW)

def LD_3D():
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(85.0,float(w)/float(h), 0.001, 1000)
	lookAt()
	glMatrixMode(GL_MODELVIEW)

def LD_4D():
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(85, float(w) / h, .000001, 1000)
	lookAt()
	glMatrixMode(GL_MODELVIEW)

def Controls():
	for event in pygame.event.get():
		if event.type == pygame.KEYUP:	LD_2D()
		if event.type == pygame.KEYDOWN:	LD_3D()
		if event.type == pygame.K_LEFT:	LD_4D()
		if event.type == pygame.QUIT:	pygame.quit()
		if event.type == pygame.K_SPACE:	pygame.quit()


# store current matrix
glMatrixMode( GL_PROJECTION );
glLoadIdentity();
# restore current matrix
glMatrixMode( GL_MODELVIEW );	#glCallList(LD_CL)

clock = pygame.time.Clock()

color = pygame.Color('white')

#start_button = pygame.draw.rect(surface,(0,0,0),(150,90,100,50));
#quit_button = pygame.draw.rect(surface,(0,0,0),(150,230,100,50));
smallfont = pygame.font.SysFont('Arial',35)
image = pygame.image.load('media/checkers12.jpg')

while True:
	dt = clock.tick(FPS) / 1000
	Controls()
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glDrawBuffer(GL_FRONT)
	glDrawBuffer(GL_BACK)
	glCallList(LD)

	rect = pygame.draw.rect(screen, (255,255,0), pygame.Rect(10, 10, 60, 60))
	text = smallfont.render('quit' , 0, color)
	#text.set_alpha(50)
	#surface.fill(color)
	surface = pygame.Surface((150, 150))
	surface.fill(color)
	surface.blit(image, (10,10))
	pygame.draw.circle(screen, (0,0,0), (25,25),25)
	pygame.display.flip ()
	#pygame.time.wait(10)

	#glFlush()
