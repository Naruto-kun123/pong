import pygame
from pygame.sprite import Sprite

class Player(Sprite):
	def __init__(self,screen,ai_settings,toggle):
		super().__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		self.toggle=toggle
		self.rect=pygame.Rect(0,0,ai_settings.paddle_width,ai_settings.paddle_height)
		self.screen_rect=screen.get_rect()
		self.rect.centery=self.screen_rect.centery
		if toggle=="Player1":
			self.rect.left=0
			self.color=ai_settings.paddle1_color
		elif toggle=="Player2":
			self.rect.right=ai_settings.screen_width
			self.color=ai_settings.paddle2_color

		self.moving_up=False
		self.moving_down=False

	def draw_paddle(self):
		pygame.draw.rect(self.screen,self.color,self.rect)

	def update(self):
		if self.moving_up and self.rect.top>0:
			self.rect.centery-=self.ai_settings.paddle_speed
		elif self.moving_down and self.rect.bottom<=self.ai_settings.screen_height:
			self.rect.centery+=self.ai_settings.paddle_speed
			