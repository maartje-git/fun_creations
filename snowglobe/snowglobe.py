# =============================================================================
# Author: Maartje Brouwer
# # Make a grid of snowflakes and let them fall down.
# # when a snowflake disappears off the bottom of the screen, make a new 
# # random flake appear at the top of the screen at a random place and let it 
# # fall.
# =============================================================================

#### Import necesarry packages
import pygame
import sys
from pygame.sprite import Group, Sprite
import random


class Drop(Sprite):
	"""A class to represent a single raindrop."""
	
	def __init__(self, screen, image):
		"""Initialize the drop and set its starting position."""
		super(Drop, self).__init__()
		self.screen = screen
		self.image = image
		
		#Load an image and set its rect attribute.
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (30, 30))
		self.rect = self.image.get_rect()
		
		#Start new star near the top-left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

	def blitme(self):
		"""Draw the raindrop at its current location."""
		self.screen.blit(self.image, self.rect)


def create_drop(screen, rain):
	"""Create a drop and place it in a row"""
	rn = random.randint(1,5)
	if rn == 1:
		image = 'snowflake-31031.png'
	elif rn == 2:
		image = 'snowflake-152419.png'
	elif rn == 3:
		image = 'snowflake-295195.png'
	elif rn == 4:
		image = 'snowflake-295196.png'
	elif rn == 5:
		image = 'snowflake-34662_640.png'
	drop = Drop(screen, image)
	screen_rect = screen.get_rect()
	screen_width = screen_rect.width
	screen_height = screen_rect.height
	#position drop
	drop.rect.x = random.randint(1, screen_width)
	drop.rect.y = random.randint(1, screen_height)
	rain.add(drop)

def create_rain(screen, rain):
	"""Create a rainy day."""
	for number in range(0,100):
		create_drop(screen, rain)

def update_rain(screen, rain):
	"""Let drops fall."""
	check_edge(screen, rain)
	for drop in rain.sprites():
		drop.rect.y += 1
	rain.update()

def check_edge(screen, rain):
	"""Check if raindrop reaches bottom of the screen."""
	screen_rect = screen.get_rect()
	screen_bottom = screen_rect.bottom
	for drop in rain.copy():
		if drop.rect.bottom > screen_bottom:
			rain.remove(drop)
			create_new_drop(screen, rain)

def create_new_drop(screen, rain):
	"""Create a new drop, that appears on the top of the screen."""
	rn = random.randint(1,5)
	if rn == 1:
		image = 'snowflake-31031.png'
	elif rn == 2:
		image = 'snowflake-152419.png'
	elif rn == 3:
		image = 'snowflake-295195.png'
	elif rn == 4:
		image = 'snowflake-295196.png'
	elif rn == 5:
		image = 'snowflake-34662_640.png'
	new_drop = Drop(screen, image)
	screen_rect = screen.get_rect()
	screen_width = screen_rect.width
	new_drop.rect.x = random.randint(1, screen_width)
	new_drop.rect.y = 1
	rain.add(new_drop)

def run_game():
	"""Initialize screen and create a screen object."""
	pygame.init()
	screen = pygame.display.set_mode((1200, 600))
	pygame.display.set_caption("Snowy Day                 by Maartje")
	bg_color = (46, 52, 86)
	rain = Group()
	create_rain(screen, rain)
	border = pygame.image.load('tree-borders-4892582.png')
	border_rect = border.get_rect()
	screen_rect = screen.get_rect()
	border_rect.centerx = screen_rect.centerx
	border_rect.bottom = screen_rect.bottom

	#start main loop of the game
	while True:
		#watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit() | sys.exit()
		#Make the most recently drawn screen visible.
		screen.fill(bg_color)
		update_rain(screen, rain)
		rain.draw(screen)
		screen.blit(border , border_rect)
		pygame.display.flip()

run_game()


