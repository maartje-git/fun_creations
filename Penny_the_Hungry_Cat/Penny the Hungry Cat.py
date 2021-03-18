# =============================================================================
# Author: Maartje Brouwer
# # Create a game that places a character that you can move left and right at 
# # the bottom of the screen. Make a ball appear at a random position at the 
# # top of the screen and fall down the screen at a steady rate. If your 
# # character “catches” the ball by colliding with it, make the ball disappear. 
# # Make a new ball each time your character catches the ball or whenever 
# # the ball disappears off the bottom of the screen.
# =============================================================================

#### Import necesarry packages
import pygame
import sys
import pygame.font
import json
from pygame.sprite import Group
from pygame.sprite import Sprite
import random


class GameStats():
	"""Track statistics for game."""
	def __init__(self, game_settings):
		"""Initialize statistics."""
		self.game_settings = game_settings
		self.reset_stats()
		with open('high_score.json') as f_o:
			self.high_score = json.load(f_o)
		self.game_active = False

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.game_settings.missed = 0
		self.game_settings.score = 0


class Settings():
	"""A class to store all settings."""

	def __init__(self):
		"""Initialize the static game's settings."""
		#Screen settings
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (124, 196, 255)
		self.wallpaper = 'wallpaper.png'
		#Score
		self.missed = 0
		self.score = 0
		self.lives = 9
		#lvl up settings
		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize the dynamic game's settings."""
		self.lvl = 1
		#ship settings
		self.penny_speed_factor = 12
		#treat settings
		self.amount_of_treats = 3
		self.treat_speed_factor = 6

	def lvl_up(self):
		"""Increase speed and amount of treats at lvl up."""
		self.lvl += 1
		self.penny_speed_factor *= self.speedup_scale
		self.amount_of_treats *= self.speedup_scale
		self.treat_speed_factor *= self.speedup_scale


class Penny():
	def __init__(self, screen, image, game_settings):
		"""Initialize a figure, place it on the screen."""
		self.screen = screen
		self.game_settings = game_settings
		#load image of figurem
		self.image = pygame.image.load(image)
		#get rect of figure and screen
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		#Start figure at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		#Store decimal values for the figure's center
		self.center = float(self.rect.centerx)

		#status of movement flag
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Updates Penny's position center value."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.game_settings.penny_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.game_settings.penny_speed_factor
		#update rect object from self.center
		self.rect.centerx = int(self.center)

	def blitme(self):
		"""draw the ship at the starting location."""
		self.screen.blit(self.image,self.rect)


class Treat(Sprite):
	"""A class to represent a single treat."""
	def __init__(self, screen, game_settings, rn):
		super(Treat, self).__init__()
		self.screen = screen
		self.game_settings = game_settings
		self.rn = rn
		if self.rn == 1:
			image = 'bird.png'
		elif self.rn == 2:
			image = 'fish.png'
		elif self.rn == 3:
			image = 'mouse.png'
		#Load an image and set its rect attribute.
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		
		#Start new treat near the top-left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#Store treats exact decimal position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
	def blitme(self):
		"""Draw the treat at its current location."""
		self.screen.blit(self.image, self.rect)


class ScoreButton():
	def __init__(self, game_settings, screen, msg, lvl, color, font_size):
		"""Initialize button attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.msg_color = color
		self.font = pygame.font.SysFont('Consolas', font_size)
		#Build the button's rect object and center it.
		self.image = pygame.image.load('score_button.png')
		self.rect = self.image.get_rect()
		self.rect.right = self.screen_rect.right - 10
		self.rect.bottom = self.screen_rect.bottom 
		#What message should the button say
		self.prep_msg(msg, lvl)

	def prep_msg(self, msg, lvl):
		"""Turn msg into a rendered image and center text on the button."""
		self.score_image = self.font.render("treats", True, (0, 0, 0))
		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.centerx = self.rect.centerx
		self.score_image_rect.top = self.rect.top + 5
		self.msg_image = self.font.render(msg, True, self.msg_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.centerx = self.rect.centerx
		self.msg_image_rect.centery = self.rect.top + 56
		self.lvl_image = self.font.render("Level: " + lvl, True, (225,0,0))
		self.lvl_image_rect = self.lvl_image.get_rect()
		self.lvl_image_rect.centerx = self.rect.centerx
		self.lvl_image_rect.top = self.rect.top + 75

	def draw_button(self):
		"""Draw a blank button and then draw the text."""
		self.screen.blit(self.image, self.rect)
		self.screen.blit(self.score_image, self.score_image_rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		self.screen.blit(self.lvl_image, self.lvl_image_rect)
		
class PlayButton():
	def __init__(self, game_settings, screen, msg):
		"""Initialize button attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#Make a start button image
		self.start = pygame.image.load('start.png')

		#Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, 200, 50)
		self.rect.right = self.screen_rect.right - 50
		self.rect.bottom = self.screen_rect.bottom - 100

	def draw_button(self):
		"""Draw the button overlay."""
		self.screen.blit(self.start, self.rect)

#Game_functions
def check_keydown_events(stats, event, penny, game_settings):
	"""Respond to keypresses."""
	if event.key == pygame.K_RIGHT:
		#set rightflag to True
		penny.moving_right = True
	elif event.key == pygame.K_LEFT:
		#set leftflag to True
		penny.moving_left = True
	elif event.key == pygame.K_p and not stats.game_active:
		stats.reset_stats()
		game_settings.initialize_dynamic_settings()
		stats.game_active = True
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, penny):
	"""Respond to key releases."""
	if event.key == pygame.K_RIGHT:
		#set rightflag to False
		penny.moving_right = False
	elif event.key == pygame.K_LEFT:
		#set leftflag to False
		penny.moving_left = False

def check_events(penny, game_settings, stats, playbutton):
	"""Responds to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.display.quit() | sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(stats, event, penny, game_settings)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, penny)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_playbutton(game_settings, stats, playbutton, mouse_x, mouse_y)

def check_playbutton(game_settings, stats, playbutton, mouse_x, mouse_y):
	"""Start a new game when the player clicks play."""
	if (playbutton.rect.collidepoint(mouse_x, mouse_y)
		and not stats.game_active):
		#Hide mouse cursor during play
		pygame.mouse.set_visible(False)
		#reset stats for new game
		stats.reset_stats()
		#reset game settings
		game_settings.initialize_dynamic_settings()
		stats.game_active = True

def create_treat(game_settings, screen, treats):
	"""Create a treat and place it somewhere on th x-axis."""
	rn = random.randint(1,3)
	treat = Treat(game_settings, screen, rn)
	screen_rect = screen.get_rect()
	screen_width = screen_rect.width
	treat.rect.centerx = random.randint(25, screen_width - 25)
	treat.rect.y = random.randint(-400,1)
	treats.add(treat)

def remove_refresh_treats(game_settings, screen, treats, penny):
	"""check if treats reach ground or Penny and remove them."""
	screen_rect = screen.get_rect()
	screen_bottom = screen_rect.bottom

	for treat in treats.copy():
		#If treat is missed, remove and add 1 to missed
		if treat.rect.bottom > screen_bottom:
			treats.remove(treat)
			game_settings.missed += 1
		#If treat is caught, remove and add 1 to score
		if pygame.sprite.spritecollide(penny, treats, True):
			game_settings.score += 1
			#lvl up every 10 caught treats
			if game_settings.score % 10 == 0:
				game_settings.lvl_up()
	#When the number of treats doesn't reach the pre-set amount of treats
	#Create a new treat
	if (len(treats) < game_settings.amount_of_treats
		and game_settings.missed < game_settings.lives):
		create_treat(game_settings, screen, treats)

def update_treats(game_settings, screen, treats, penny):
	"""Update the position of all treats on the screen."""
	for treat in treats.sprites():
		treat.rect.y += int(game_settings.treat_speed_factor)
	treats.update()
	remove_refresh_treats(game_settings, screen, treats, penny)

def update_lives(screen, game_settings, treats, stats):
	"""Show how many lives Pwenny has left."""
	missed = game_settings.missed
	lives = game_settings.lives
	lives_left = lives - missed
	heart = 'heart.png'
	for life in range (lives_left):
		lives_game = pygame.image.load(heart)
		lives_game_rect = lives_game.get_rect()
		lives_game_rect.right = 50 
		lives_game_rect.top = 5 + life * lives_game_rect.height
		screen.blit(lives_game, lives_game_rect)
	if missed == lives + 1:
		game_over(game_settings, screen, treats, stats)

def update_score(game_settings, screen):
	"""Updates the current score board."""
	#Show how many treats were caught.
	msg = str(game_settings.score)
	lvl = str(game_settings.lvl)
	color = (124, 196, 255)
	font_size = 30
	score = ScoreButton(game_settings, screen, msg, lvl, color, font_size)
	score.draw_button()

def final_score(game_settings, screen, stats):
	"""After game-over, show score and high score."""
	screen_rect = screen.get_rect()
	#Nice sign
	score = pygame.image.load('signpost.png')
	score_rect = score.get_rect()
	score_rect.left = 100
	score_rect.top = screen_rect.top + 10
	screen.blit(score, score_rect)
	#Write down score of this game
	font = pygame.font.SysFont('Consolas', 30)
	score_image = font.render("Treats caught: " + str(game_settings.score),
		True, (0,0,0))
	score_image_rect = score_image.get_rect()
	score_image_rect.centerx = score_rect.centerx
	score_image_rect.top = score_rect.top + 30
	screen.blit(score_image, score_image_rect)
	#If score > high_score cheer and save new high score
	if game_settings.score > stats.high_score:
		cheers = font.render("NEW HIGHSCORE!!!", True, (225,0,0))
		cheers_rect = cheers.get_rect()
		cheers_rect.centerx = score_rect.centerx
		cheers_rect.centery = score_rect.centery
		screen.blit(cheers, cheers_rect)
		with open('high_score.json', 'w') as f_o:
			json.dump(game_settings.score, f_o)
	#show high score
	with open('high_score.json') as f_o:
		high_score = json.load(f_o)
	highscore_image = font.render("HighScore: " + str(high_score),
		True, (0,0,0))
	highscore_image_rect = highscore_image.get_rect()
	highscore_image_rect.centerx = score_rect.centerx
	highscore_image_rect.bottom = score_rect.bottom - 30
	screen.blit(highscore_image, highscore_image_rect)

def game_over(game_settings, screen, treats, stats):
	"""
	When all lives are lost, remove all treats 
	Show game_over + score + high score 
	Change game_activity status to False
	"""
	treats.empty()
	#Show empty screen
	screen.fill(game_settings.bg_color)
	border1 = pygame.image.load('grass1.png')
	border2 = pygame.image.load('grass2.png')
	screen_rect = screen.get_rect()
	border1_rect = border1.get_rect()
	border1_rect.centerx = screen_rect.centerx
	border1_rect.bottom = screen_rect.bottom
	border2_rect = border2.get_rect()
	border2_rect.centerx = screen_rect.centerx
	border2_rect.bottom = screen_rect.bottom
	screen.blit(border1, border1_rect)
	screen.blit(border2 , border2_rect)
	#Show final score on a nice sign
	final_score(game_settings, screen, stats)
	#Show Game Over sign
	game_over = pygame.image.load('game_over.png')
	game_over_rect = game_over.get_rect()
	game_over_rect.centerx = screen_rect.centerx
	game_over_rect.centery = screen_rect.centery + 50
	screen.blit(game_over, game_over_rect)
	#show game logo
	title = pygame.image.load('penny_the_hungry2.png')
	title = pygame.transform.scale(title, (500, 185))
	title_rect = title.get_rect()
	title_rect.right = screen_rect.width - 40
	title_rect.top = 40
	screen.blit(title, title_rect)
	#Change game_active status t false to stop the loop
	stats.game_active = False
	pygame.mouse.set_visible(True)


#Main program
def run_game():
	"""Initialize game and create screen objects."""
	pygame.init()
	game_settings = Settings()
	screen = pygame.display.set_mode(
		(game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption(
		"Pennywise the Hungry cat                     a game by Maartje")
	#Make Penny
	penny = Penny(screen, 'cat.png', game_settings)
	#make wallpaper
	wallpaper = pygame.image.load(game_settings.wallpaper)
	wallpaper_rect = screen.get_rect()
	#make grass border
	border1 = pygame.image.load('grass1.png')
	border2 = pygame.image.load('grass2.png')
	screen_rect = screen.get_rect()
	border1_rect = border1.get_rect()
	border1_rect.centerx = screen_rect.centerx
	border1_rect.bottom = screen_rect.bottom
	border2_rect = border2.get_rect()
	border2_rect.centerx = screen_rect.centerx
	border2_rect.bottom = screen_rect.bottom
	#new game screen
	title = pygame.image.load('penny_the_hungry.png')
	title_rect = title.get_rect()
	title_rect.centerx = screen_rect.centerx
	title_rect.bottom = screen_rect.bottom - 30
	#Make a group of treats
	treats = Group()
	create_treat(game_settings, screen, treats)
	#Create an instance to store GameStats
	stats = GameStats(game_settings)
	playbutton = PlayButton(game_settings, screen, "PLAY")

	#start main loop of the game 
	while True:
		#watch for keyboard and mouse events
		check_events(penny, game_settings, stats, playbutton)
		#Title screen
		screen.blit(wallpaper, wallpaper_rect)
		screen.blit(border1, border1_rect)
		screen.blit(title, title_rect)
		screen.blit(border2 , border2_rect)
		#during the game
		if stats.game_active:
			screen.blit(wallpaper, wallpaper_rect)
			screen.blit(border1, border1_rect)
			#Update position of Penny
			penny.update()
			#What's the score
			update_score(game_settings, screen)
			#update position treat
			update_treats(game_settings, screen, treats, penny)	
			#Draw Penny
			penny.blitme()
			#Draw treat
			treats.draw(screen)
			screen.blit(border2 , border2_rect)
		#Draw how many lives left
		update_lives(screen, game_settings, treats, stats)
		if not stats.game_active:
			playbutton.draw_button()
		pygame.display.flip()

run_game()
