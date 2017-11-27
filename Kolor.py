import os, sys, pygame

#execfile('file.py')
main_dir = os.path.split(os.path.abspath(__file__))[0]
platformer_dir = os.path.join(main_dir, 'platformer')
space_dir = os.path.join(main_dir, 'python game stuff')
pong_dir = os.path.join(main_dir, 'pong')
starjump_dir = os.path.join(main_dir, 'StarJump')

clock = pygame.time.Clock() 
SCREENRECT = pygame.Rect(0, 0, 640, 480)
BLACK = (0,0,0)
WHITE = (255,255,255)

def load_sprite(file, colorkey=-1):
	"loads an image, prepares it for play"
	if not pygame.image.get_extended(): 
		raise SystemExit("Could not load image; extended images not available")
	image_to_load = os.path.join(main_dir, 'data', file)
	try:
		image_export = pygame.image.load(image_to_load)
	except pygame.error as message:
		print ('Could not load image')
		raise SystemExit(message)
	image_export = image_export.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image_export.get_at((0,0))
		image_export.set_colorkey(colorkey)
	return image_export, image_export.get_rect()

def launch_game(name):
	_platformer = platformer_dir + "\platformer.py"
	os.system(_platformer)
	
class Button(pygame.sprite.Sprite):
	passedname = ""
	"""menu button"""
	def __init__(self,passedimage,passedmidbottom):
		pygame.sprite.Sprite.__init__(self,self.containers) #call Sprite intializer
		self.image = passedimage
		self.rect = self.image.get_rect(midbottom=passedmidbottom)
		self.origtop = self.rect.top
		
	def clicked(self):
		launch_game("platformer")

class Mouse(pygame.sprite.Sprite):
	"""mouse"""
	def __init__(self,passedimage,passedmidbottom):
		pygame.sprite.Sprite.__init__(self) #call Sprite intializer
		screen = pygame.display.get_surface()
		self.image = passedimage
		self.rect = self.image.get_rect(midbottom=passedmidbottom)
		self.origtop = self.rect.top
		self.clicking = 0

	def update(self):
		"move the cursor based on the mouse position"
		pos = pygame.mouse.get_pos()
		self.rect.midtop = pos
		if self.clicking:
			self.rect.move_ip(5, 10)

	def click(self, target):
		"returns true if the cursor collides with the target"
		if not self.clicking:
			self.clicking = 1
			hitbox = self.rect.inflate(-5, -5)
			return hitbox.colliderect(target.rect)

	def unclick(self):
		self.clicking = 0
		
def main(winstyle = 0):	
	pygame.init()
	pygame.display.set_caption('Kolor')
	bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
	screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
	background = pygame.Surface(SCREENRECT.size)
	screen.fill(WHITE)
	background.fill(WHITE)
	screen.blit(background, (0,0))
	pygame.display.flip()
	

	#sprite groups
	button_list = pygame.sprite.Group()
	all = pygame.sprite.RenderUpdates()
	Button.containers = button_list, all
	
	if pygame.font:
		font = pygame.font.Font(None, 36)
		text = font.render("KOLOR", 1, (10, 10, 10))
		textpos = text.get_rect(centerx=background.get_width()/2)
		background.blit(text, textpos)
	
	avatar = load_sprite('avatar.png', -1)
	buttonsprite = load_sprite('button.jpg', -1)
	
	mouse = Mouse(avatar[0],SCREENRECT.midbottom)
	#button = Button(buttonsprite[0],SCREENRECT.midbottom)
	
	#rleft = SCREENRECT.left - 200
	#rtop = SCREENRECT.bottom - 128
	#buttonrect = pygame.Rect(rleft,rtop,16,16)
	#button = Button(avatar[0],buttonrect)
	#button = Button(buttonsprite[0],buttonrect)
	#button = Button(avatar[0],SCREENRECT.midbottom)
	button = Button(buttonsprite[0],SCREENRECT.midbottom)
		
	while 1:
		all.clear(screen,background) #clean screen
		all.update() #reset sprites
		
		#input
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				return
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if mouse.click(button):
					print("hit")
					button.clicked()
				else:
					print("missed")
			elif event.type == pygame.MOUSEBUTTONUP:
				mouse.unclick()

		#Draw Everything
		screen.blit(background, (0, 0))
		pygame.display.flip()
		
		dirty = all.draw(screen)
		pygame.display.update(dirty)
		clock.tick(60)	
		
		
if __name__ == '__main__':
	main()