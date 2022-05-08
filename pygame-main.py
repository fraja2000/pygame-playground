import sys
from ball import Ball
import pygame
from pygame import FULLSCREEN
from pygame.time import Clock

pygame.init()
screen = pygame.display.set_mode((0, 0), FULLSCREEN)
screen_width, screen_height = screen.get_size()
screen_width = screen_width
screen_height = screen_height
blue = 0, 0, 255
black = 0, 0, 0
clock = Clock()

font_type = pygame.font.Font('freesansbold.ttf', 20)

# create balls
ball_1 = Ball(100, 500, 1, 1)
ball_2 = Ball(200, 400, 52, 23, 0.6)
ball_3 = Ball(300, 300, 5, 35, 0.5)
ball_4 = Ball(400, 200, 10, 20, 0.95)
ball_5 = Ball(500, 100, 8, 7)
balls = [ball_1, ball_2, ball_3, ball_4, ball_5]
# balls = [ball_1]
while True:

    # timeDelta = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            sys.exit()

    # update balls
    for ball in balls:
        ball.update_model(screen_width, screen_height)

    screen.fill(black)
    # draw balls
    for ball in balls:
        ball.draw(screen)

    text_on_screen = font_type.render(Ball.get_bounces_text(), True, blue, black)
    rect_for_text = text_on_screen.get_rect()
    rect_for_text.center = (screen_width // 2, screen_height // 2)
    screen.blit(text_on_screen, rect_for_text)

    pygame.display.update()
    pygame.time.delay(20)
