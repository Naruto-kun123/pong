import pygame.font

class Scoreboard():
	def __init__(self,screen,ai_settings):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.ai_settings=ai_settings

		self.text_color=(0,230,0)
		self.font=pygame.font.Font("prstartk.ttf",20)

		self.prep_score()

	def prep_score(self):
		score_p1=str(self.ai_settings.score_p1)
		score_p2=str(self.ai_settings.score_p2)

		self.image_p1=self.font.render(score_p1,True,self.text_color,self.ai_settings.bg_color)
		self.image_p2=self.font.render(score_p2,True,self.text_color,self.ai_settings.bg_color)

		self.image_p1_rect=self.image_p1.get_rect()
		self.image_p2_rect=self.image_p2.get_rect()
		self.image_p1_rect.top=20
		self.image_p2_rect.top=20
		self.image_p1_rect.left=self.screen_rect.left+20
		self.image_p2_rect.right=self.screen_rect.right-20

	def show_score(self):
		self.screen.blit(self.image_p1,self.image_p1_rect)
		self.screen.blit(self.image_p2,self.image_p2_rect)

