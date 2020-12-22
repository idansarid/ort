import pygame
import random
from shape.Ball import Ball

WIDTH = 720
HEIGHT = 720
LEFT = 1
REFRESH_RATE = 60
BALL_SIZE = 55 # pixels

img = pygame.image.load('nature.jpg')
pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
myriadProFont = pygame.font.SysFont("Myriad Pro", 48)
helloWorld = myriadProFont.render("Hello world!", 1, (255, 0, 255), (255, 255, 255))

screen.blit(helloWorld, (0, 0))
clock = pygame.time.Clock()

balls_list = pygame.sprite.Group()
new_balls_list = pygame.sprite.Group()

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            ball = Ball(x, y)
            vx = random.randint(-3, 3)
            vy = random.randint(-3, 3)
            ball.update_v(vx, vy)
            balls_list.add(ball)
    for ball in balls_list:
        ball.update_loc()
        x, y = ball.get_pos()
        vx, vy = ball.get_v()
        if x + ball.image_size[0] > WIDTH or x <= 0:
            vx *= -1

        if y + ball.image_size[1] > HEIGHT or y <= 0:
            vy *= -1

        ball.update_v(vx, vy)

    new_balls_list.empty()
    for ball in balls_list:
        balls_hit_list = pygame.sprite.spritecollide(ball, balls_list, False)
        if len(balls_hit_list) == 1:
            new_balls_list.add(ball)

    balls_list.empty()
    for ball in new_balls_list:
        balls_list.add(ball)

    screen.blit(img, (0, 0))
    balls_list.draw(screen)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)

pygame.quit()