import os, sys
import pygame

#debug errors and shit
if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')
if not pygame.image.get_extended(): print ('Warning, images disabled')

#store the path to our shit for the functions
main_dir = os.path.split(os.path.abspath(__file__))[0]

"""***********************
Game functions
***********************"""

def load_music(file):
	"loads a sound file, prepares it for play"
	class NoneSound:
		def play(self): pass
	if not pygame.mixer:
		return NoneSound()
	sound_to_load = os.path.join(main_dir, 'data', file)
	try:
		audio_export = pygame.mixer.music.load(sound_to_load)
	except pygame.error as message:
		print ('Cannot load audio file')
		print ('tried to load the following;')
		print (sound_to_load)
		print ('Error message:')
		raise SystemExit(message)
	return audio_export

def load_image(file, colorkey=-1):
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

"""***********************
More constants
***********************"""


"""***********************
classes & sprites
***********************"""

class Pentagon(pygame.sprite.Sprite):
	"""It's our player pentagon"""
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.image, self.rect = avatar
	
	def update(self):
        #movecode goes here
		mymove = 0

class Wall(pygame.sprite.Sprite):
	#black rectangle, stops movement
	mywall = (255,255,255)

class Pit(pygame.sprite.Sprite):
	#white (tansparent?) rectangle, allows movement
	mypit = (0,0,0)

"""***********************
Primary loop
***********************"""

#Shouldn't this be Main() or something?
def main():
	#Let's hit it!
	pygame.init()
	clock = pygame.time.Clock()
	
	#setup the screen.
	screen = pygame.display.set_mode((640, 480))
	screen.fill((255, 255, 255))
	pygame.display.set_caption('Kolor - Plato')

	#stores width/height as vars... redundant?
	screenwidth, screenheight = pygame.display.get_surface().get_size()
	#other common vars for the map design
	commonheight = screenheight//10
	screenbottom = screenheight - commonheight
	
	gameover = False
	initgame = False
		
	avatar = load_image('avatar.png', -1)
	while not gameover:
		#we define everything here so we can restart the game with a keybind.
		#if we don't want the keybind, we can move it up to before the loop!
		if not initgame:
			avatar_x = 30
			avatar_y = 30
			#screen.blit(avatar, (avatar_x,avatar_y))
			load_music('cityruins.mp3')
			pygame.mixer.music.play(-1)
			"""setup level
			remember, it's (screen, color, rectangle(left, top, width, height), "width" aka donotfill)
			use the vars as an anchor point, eg screenbottom - 20"""
			floor = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, screenbottom, screenwidth, commonheight)) #the floor
			wall1 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(100, screenbottom - 20, 10, 20)) # a wall!
			wall2 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(300, screenbottom - 40, 20, 40)) # another wall!
			initgame = True
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameover = True
				print("Recieved quit command.")
		pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(avatar_x, avatar_y, 16, 16))
		pressed = pygame.key.get_pressed()
		"""something like if avatar_y + 3 != dangerzone... how do
		we even define the dangerzone? check against the floor and walls every time?
		assign rectangles as the dangerzone, check if values are similar...?"""
		"""pygame.sprite.Sprite is the function we want to use for this.
		https://www.pygame.org/docs/ref/sprite.html"""
		#if pressed[pygame.K_UP]: avatar_y -= 3
		if avatar_y < (screenbottom - 18):
			avatar_y += 3
			#acceleration?
		if pressed[pygame.K_DOWN]: avatar_y += 3
		if pressed[pygame.K_LEFT]: 
			print(wall1)
			#if not ((avatar_x - 3) == wall1):
				#avatar_x -= 3
		if pressed[pygame.K_RIGHT]: 
			print(wall2)
			#if not ((avatar_x + 3) == wall1):
				#avatar_x += 3
		if pressed[pygame.K_r]: 
			initgame = False
			pygame.mixer.music.stop()
		#screen.blit(avatar, (avatar_x,avatar_y))
		pygame.display.flip()
		clock.tick(120)
		
if __name__ == '__main__': main()