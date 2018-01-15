import sys, pygame
from settings import Settings
from ball import Ball
import game_functions as gf
from player import Player
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    p1=Player(screen,ai_settings,"Player1")
    p2=Player(screen,ai_settings,"Player2")
    bb=Button(screen,ai_settings,"HIT A KEY TO PLAY")
    bb2=Button(screen,ai_settings,"GAME OVER. HIT A KEY")
    bb3=Button(screen,ai_settings,"")
    sb=Scoreboard(screen,ai_settings)
    ball=Ball(screen,ai_settings,sb)


    while True:
        gf.check_events(ai_settings,ball,p1,p2,bb)
        if ai_settings.game_on:
            ball.update(sb)
            p1.update()
            p2.update()
            if ai_settings.lives_p1 ==0 or ai_settings.lives_p2 ==0:
                print ("GAME OVER!")
                ai_settings.series+=1
                if ai_settings.lives_p1==0:
                    print ("Player 2 wins!")
                elif ai_settings.lives_p2==0:
                    print ("Player 1 wins!")
                gf.score_reset(ai_settings)
                ai_settings.series+=1
        gf.update_screen(screen,ai_settings,ball,p1,p2,bb,bb2,sb)



run_game()