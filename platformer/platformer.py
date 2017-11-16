import os
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
#stores width/height as vars... redundant?
screenwidth, screenheight = pygame.display.get_surface().get_size()
commonheight = screenheight//10
screenbottom = screenheight - commonheight
print(screenwidth, screenheight, commonheight, screenbottom) ###debug
screen.fill((255, 255, 255)) #make this white dingus
clock = pygame.time.Clock()

avatar = pygame.image.load('avatar.png')

gameover = False
initgame = False
while not gameover:
	if not initgame:
		avatar_x = 30
		avatar_y = 30
		screen.blit(avatar, (avatar_x,avatar_y))
		pygame.mixer.music.load('cityruins.mp3')
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
	screen.blit(avatar, (avatar_x,avatar_y))
	pygame.display.flip()
	clock.tick(120)