import pygame,sys
from button import Button

def check_events(ai_settings,ball,player1,player2,button):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		if event.type==pygame.KEYDOWN:
			check_keydown_events(event,player1,player2)
		if event.type==pygame.KEYUP:
			check_keyup_events(event,player1,player2)
		if event.type==pygame.MOUSEBUTTONDOWN:
			mouseposx,mouseposy=pygame.mouse.get_pos()
			press_play(ai_settings,button,mouseposx,mouseposy)
		if event.type==pygame.KEYDOWN and ai_settings.game_on==False: ai_settings.game_on=True

	paddle_collide(ai_settings,ball,player1,player2)

def check_keydown_events(event,player1,player2):
	if event.key==pygame.K_q:
		sys.exit()

	if event.key==pygame.K_a:
		player1.moving_up=True
	if event.key==pygame.K_z:
		player1.moving_down=True

	if event.key==pygame.K_k:
		player2.moving_up=True
	if event.key==pygame.K_m:
		player2.moving_down=True


def check_keyup_events(event,player1,player2):
	if event.key==pygame.K_a:
		player1.moving_up=False
	elif event.key==pygame.K_z:
		player1.moving_down=False

	if event.key==pygame.K_k:
		player2.moving_up=False
	elif event.key==pygame.K_m:
		player2.moving_down=False


def update_screen(screen,ai_settings,ball,p1,p2,button,button2,sb):
	screen.fill(ai_settings.bg_color)
	if ai_settings.game_on==False and ai_settings.series==0:
		button.create_button()
	elif ai_settings.game_on==False and ai_settings.series>0:
		button2.create_button()
	else:
		ball.blitme(screen)
		p1.draw_paddle()
		p2.draw_paddle()
		ball.check_edges()
		sb.show_score()
	pygame.display.flip()

def press_play(ai_settings,button,mouseposx,mouseposy):
	button_rect=button.rect
	if button_rect.collidepoint(mouseposx,mouseposy) and ai_settings.game_on==False:
		#pygame.mouse.set_visible(False)
		score_reset(ai_settings)
		ai_settings.game_on=True

def paddle_collide(ai_settings,ball,p1,p2):
	if p1.rect.colliderect(ball.rect):
		ai_settings.speed[0] = -ai_settings.speed[0]
		ai_settings.rally_counter+=1

	if p2.rect.colliderect(ball.rect):
		ai_settings.speed[0] = -ai_settings.speed[0]
		ai_settings.speed[1] = -ai_settings.speed[1]
		ai_settings.rally_counter+=1
	
	#print (ai_settings.rally_counter, ai_settings.ball_speed_factor, "SPEED:",ai_settings.speed)
	if ai_settings.rally_counter>=ai_settings.rally_speeder:
		ai_settings.rally_counter=0
		level_up(ai_settings)

def level_up(ai_settings):
	ai_settings.ball_speed_factor+=1

def score_reset(ai_settings):
	ai_settings.lives_p1=3
	ai_settings.lives_p2=3
	ai_settings.score_p1=0
	ai_settings.score_p2=0
	ai_settings.rally_counter=0
	ai_settings.game_on=False


