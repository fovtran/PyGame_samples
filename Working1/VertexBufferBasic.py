from AllImports import *
from Init import *
import importlib
import glPerspectives

w = 640
h = 480
running = True
screen = pygame_init(w,h)

class MonkeyWatcher(object):
	def __init__(self):
		self._cached_stamp = 0
		pathname = os.path.dirname(sys.argv[0])
		self.fullpath = os.path.abspath(pathname)
		self.fn = './glPerspectives.py'
		self.filename = os.path.join(self.fullpath, self.fn)

	def ook(self):
		stamp = os.stat(self.filename).st_mtime
		if stamp != self._cached_stamp:
			self._cached_stamp = stamp
			# File has changed, so do something...
			importlib.reload(glPerspectives)
			print("Module reloaded!")

def VBO():
	glEnableClientState (GL_VERTEX_ARRAY)
	vertices = [ 0.0, .5, 0.0,  0.0, 0.0, 0.0,  .5, .5, 0.0 ]
	vbo = glGenBuffers (1)
	glBindBuffer (GL_ARRAY_BUFFER, vbo)
	glBufferData (GL_ARRAY_BUFFER, len(vertices)*4, (c_float*len(vertices))(*vertices), GL_STATIC_DRAW)
	glVertexPointer (3, GL_FLOAT, 0, None)

def draw():
	glEnableClientState (GL_VERTEX_ARRAY)
	glColor (0.05, 0.95, 0.05, 1.0)
	glDrawArrays (GL_TRIANGLES, 0, 3)
	glDisableClientState (GL_VERTEX_ARRAY)

def quit():
	running = False
	pygame.quit()
	sys.exit()

def Controls():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:	
			quit()
		if event.type == pygame.VIDEORESIZE:
			screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
			#glViewport (0, 0, w, h)
			#print(f"Window resized to: {event.w}x{event.h}")

		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:  # Quit on ESC key
			quit()
		#elif event.type == pygame.KEYDOWN:  # Handle key press
		elif keys[ pygame.K_1 ]:
			perspective = glPerspectives.Perspective(w, h)
			perspective.LD_I()		
		elif keys[ pygame.K_5 ]:
			perspective = glPerspectives.Perspective(w, h)
			perspective.LD_DEF()
		elif keys[ pygame.K_2 ]:
			perspective = glPerspectives.Perspective(w, h)
			perspective.LD_2D()
		elif keys[ pygame.K_3 ]:
			perspective = glPerspectives.Perspective(w, h)
			perspective.LD_3D()
		elif keys[ pygame.K_4 ]:
			perspective = glPerspectives.Perspective(w, h)
			perspective.LD_4D()
			#else:
				#print(f"Key pressed: {pygame.key.name(event.key)}")
		elif event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse click
			print(f"Mouse clicked at {event.pos}")

global LD
LD = glGenLists(4)
VBO()
glNewList(LD, GL_COMPILE)
draw()
glEndList()

FWATCH = MonkeyWatcher()
clock = pygame.time.Clock()
while running:
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	dt = clock.tick(FPS) / 1000
	Controls()
	glDrawBuffer(GL_FRONT)	
	glDrawBuffer(GL_BACK)
	glCallList(LD)

	pygame.display.flip()
	pygame.time.wait(25)
	FWATCH.ook()
	#glFlush()
