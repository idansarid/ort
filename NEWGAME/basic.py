import pygame
import socket
import time
import os
import math

pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = str(10) + "," + str(40)

WIDTH = 500
ROWS = 3
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("TicTacToe")

X_IMAGE = pygame.transform.scale(pygame.image.load("cross.jpg"), (150, 150))
O_IMAGE = pygame.transform.scale(pygame.image.load("circle.jpg"), (150, 150))

END_FONT = pygame.font.SysFont('courier', 40)

# colors
GREY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_grid():
    gap = WIDTH // ROWS

    x = 0
    y = 0

    for i in range(ROWS):
        x = i * gap
        pygame.draw.line(screen, GREY, (x, 0), (x, WIDTH), 3)
        pygame.draw.line(screen, GREY, (0, x), (WIDTH, x), 3)


def initialize_grid():
    dis_to_cen = WIDTH // ROWS // 2

    # Initializing the array
    game_array = [[None, None, None],
                  [None, None, None],
                  [None, None, None]]

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = dis_to_cen * (2 * j + 1)
            y = dis_to_cen * (2 * i + 1)

            # Adding centre coordinates
            game_array[i][j] = (x, y, "")

    return game_array


def render():
    screen.fill(WHITE)
    draw_grid()

    # Drawing X's and O's
    for item in images:
        x, y, IMAGE = item
        screen.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pygame.display.update()


def turn_management(x_turn, game_array, mx, my, image=X_IMAGE):
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char = game_array[i][j]

            # Distance between mouse and the centre of the square
            dis = math.sqrt((x - mx) ** 2 + (y - my) ** 2)
            if dis < WIDTH // ROWS // 2:
                if x_turn:
                    game_array[i][j] = (x, y, 'x')
                else:
                    game_array[i][j] = (x, y, 'o')
                images.append((x, y, image))


def win(game_array):
    if (game_array[0][0][2] == game_array[0][1][2] == game_array[0][2][2]) and game_array[0][0][2] != '':
        display_message("{} has won!".format(str(game_array[0][0][2])))
    elif (game_array[0][0][2] == game_array[1][0][2] == game_array[2][0][2]) and game_array[0][0][2] != '':
        display_message("{} has won!".format(str(game_array[0][0][2])))
    elif (game_array[2][0][2] == game_array[2][1][2] == game_array[2][2][2]) and game_array[2][0][2] != '':
        display_message("{} has won!".format(str(game_array[2][0][2])))
    elif (game_array[0][2][2] == game_array[1][2][2] == game_array[2][2][2]) and game_array[0][2][2] != '':
        display_message("{} has won!".format(str(game_array[0][2][2])))
    elif (game_array[0][0][2] == game_array[1][1][2] == game_array[2][2][2]) and game_array[0][0][2] != '':
        display_message("{} has won!".format(str(game_array[0][0][2])))
    elif (game_array[1][0][2] == game_array[1][1][2] == game_array[1][2][2]) and game_array[1][0][2] != '':
        display_message("{} has won!".format(str(game_array[1][0][2])))
    elif (game_array[0][1][2] == game_array[1][1][2] == game_array[2][1][2]) and game_array[0][1][2] != '':
        display_message("{} has won!".format(str(game_array[0][1][2])))
    elif (game_array[0][2][2] == game_array[1][1][2] == game_array[2][0][2]) and game_array[0][2][2] != '':
        display_message("{} has won!".format(str(game_array[0][2][2])))


def click(game_array):
    global x_turn, o_turn, images

    # Mouse position
    mx, my = pygame.mouse.get_pos()
    print(mx, my)
    if x_turn:
        turn_management(x_turn=x_turn, game_array=game_array, mx=mx, my=my, image=X_IMAGE)
        x_turn = False
        o_turn = True
    elif o_turn:
        turn_management(x_turn=x_turn, game_array=game_array, mx=mx, my=my, image=O_IMAGE)
        o_turn = False
        x_turn = True


def display_message(content):
    pygame.time.delay(500)
    screen.fill(WHITE)
    end_text = END_FONT.render(content, 1, BLACK)
    screen.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    global x_turn, o_turn, images, draw

    images = []
    draw = False

    run = True
    x_turn = True
    o_turn = False
    game_array = initialize_grid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(game_array)

        render()

        if win(game_array):
            run = False
            break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


while True:
    if __name__ == '__main__':
        main()