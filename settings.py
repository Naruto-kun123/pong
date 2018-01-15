import pygame

class Settings():

	def __init__(self):
	
		self.screen_width=800
		self.screen_height=500

		self.speed=[2,2]

		self.bg_color=0, 0, 0

		self.paddle_width=20
		self.paddle_height=100
		self.paddle1_color=255,0,0
		self.paddle2_color=255,230,0

		self.paddle_speed=10

		self.ball_speed_factor=3

		self.lives_p1=3
		self.lives_p2=3

		self.score_p1=0
		self.score_p2=0

		self.rally_counter=0
		self.rally_speeder=3

		self.game_on=False

		self.series=0

