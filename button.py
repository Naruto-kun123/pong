import pygame.font

class Button():
	def __init__(self,screen,ai_settings,msg):
		self.screen=screen
		self.screen_rect=screen.get_rect()

		self.width,self.height=ai_settings.screen_width/3,ai_settings.screen_height/10
		self.button_color=(0,0,0)
		self.button_text_color=(255,255,255)
		self.font=pygame.font.Font("prstartk.ttf",int(ai_settings.screen_width*0.03))
		self.msg=msg

		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center

		self.msg_image=self.font.render(msg,True,self.button_text_color)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center

	def create_button(self):
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)