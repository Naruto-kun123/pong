import sys, pygame
from settings import Settings
from time import sleep

class Ball():
    def __init__(self,screen,ai_settings,sb):
        self.ai_settings=ai_settings
        self.image = pygame.image.load("ball2.png")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.speed=ai_settings.speed
        self.rect.center=self.screen_rect.center
        self.sb=sb

    def blitme(self,screen):
        screen.blit(self.image,self.rect)



    def update(self,sb):
        self.rect=self.rect.move(self.speed[0]*self.ai_settings.ball_speed_factor,self.speed[1]*self.ai_settings.ball_speed_factor)
        self.check_goal(sb)


    def check_edges(self):
        if self.rect.left < 0 or self.rect.right > self.ai_settings.screen_width:
            self.ai_settings.speed[0] = -self.ai_settings.speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.ai_settings.screen_height:
            self.ai_settings.speed[1] = -self.ai_settings.speed[1]

    def check_goal(self,sb):
        if self.rect.left<=0 or self.rect.right>=self.ai_settings.screen_width:
            if self.rect.left <=0:
                self.ai_settings.score_p2+=1
                self.ai_settings.lives_p1-=1
                sb.prep_score()
                sleep(1)
            if self.rect.right >= self.ai_settings.screen_width:
                self.ai_settings.score_p1+=1
                self.ai_settings.lives_p2-=1
                sb.prep_score()
                sleep(1)
            print ("Player 1:",self.ai_settings.score_p1, "Player 2:",self.ai_settings.score_p2)
            self.ai_settings.ball_speed_factor=3
            self.rect.center=self.screen_rect.center