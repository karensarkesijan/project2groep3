import os, sys, pygame

#execfile('file.py')
main_dir = os.path.split(os.path.abspath(__file__))[0]
platformer_dir = os.path.join(main_dir, 'platformer')
data_dir = os.path.join(main_dir, 'python game stuff')
data_dir = os.path.join(main_dir, 'Platform painter')
data_dir = os.path.join(main_dir, 'data')

clock = pygame.time.Clock() 
SCREENRECT = pygame.Rect(0, 0, 640, 480)
BLACK = (0,0,0)
WHITE = (255,255,255)


def launch_game(name, unlocked=False):
	fullname = os.path.join(name, name)
	execfile(fullname)
	
class Painter(pygame.sprite.Sprite):
    """menu button"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = load_image('chimp.bmp', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
	
	
bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
background = pygame.Surface(SCREENRECT.size)
screen.fill(WHITE)
background.fill(WHITE)
screen.blit(background, (0,0))
pygame.display.flip()
	
while 1:
    clock.tick(60)	
	for event in pygame.event.get():
		if event.type == QUIT:
			return
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			return
		elif event.type == MOUSEBUTTONDOWN:
			if fist.punch(chimp):
				punch_sound.play() #punch
				chimp.punched()
			else:
				whiff_sound.play() #miss
		elif event.type == MOUSEBUTTONUP:
			fist.unpunch()