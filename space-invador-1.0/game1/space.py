import pygame
from infra.Board import Board
from infra.Player import Player
from network.client import Client
import random
import time

if __name__ == '__main__':
    p = None
    p2 = None
    client = Client()
    player_chosen = client.getPlayer()
    board = Board(player=player_chosen)
    if player_chosen == 0:
        p = Player()
        p2 = Player(x=170, y=480)
    elif player_chosen == 1:
        p2 = Player()
        p = Player(x=170, y=480)
    running = True
    count = 0
    counter = 0
    time.sleep(10)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p.playerX_change = -0.1
                if event.key == pygame.K_RIGHT:
                    p.playerX_change = 0.1
                if event.key == pygame.K_UP:
                    p.playerY_change = -0.1
                if event.key == pygame.K_DOWN:
                    p.playerY_change = 0.1
                if event.key == pygame.K_SPACE:
                    if board.bullet.bullet_state == "ready":
                        board.bullet.x = p.x
                        board.bullet.y = p.y
                        board.fire_bullet(board.bullet.x, board.bullet.y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    p.playerX_change = 0
                    p.playerY_change = 0

        if board.win:
            running = False
            continue

        board.screen.fill((0, 0, 0))
        board.screen.blit(board.background, (0, 0))
        p.move()
        ################### Network #################################################
        if count % 10 == 0:
            aa = client.send("Coordinates: {} {}".format(p.x, p.y))
            print(aa)
            count = 0
        count += 1
        ############################################################################
        # boundaries of space ships
        p.boundary_check()
        for enemy in board.enemies:
            enemy.move()

        # bullet handling
        if board.bullet.y <= 0:
            board.bullet.y = 480
            board.bullet.bullet_state = "ready"
        elif board.bullet.bullet_state == "fire":
            board.fire_bullet(board.bullet.x, board.bullet.y)
            board.bullet.y -= board.bullet.bulletY_change

        for enemy in board.enemies:
            if board.is_collision(x2=enemy.x, x1=board.bullet.x, y2=enemy.y, y1=board.bullet.y):
                board.bullet.y = 480
                board.bullet.bullet_state = "ready"
                ################### Network #################################################
                if player_chosen == 0:
                    board_score1 = client.send("AddOne 1")
                    board.score1 = int(board_score1)
                elif player_chosen == 1:
                    board_score2 = client.send("AddTwo 1")
                    board.score2 = int(board_score2)
                ############################################################################
                enemy.hit_count += 1
                enemy.x = random.randint(0, 735)
                enemy.y = random.randint(50, 150)

        scores_from_server = client.send("Score 1")
        board_score_list = scores_from_server.replace("]", "").replace("[", "").split(",")
        board.score1 = int(board_score_list[0])
        board.score2 = int(board_score_list[1])
        res = None
        if player_chosen == 0:
            res = client.send("getName 1")
        elif player_chosen == 1:
            res = client.send("getPlayerData 0")
        try:
            coor = res.split()
        except:
            continue
        board.player_blit(float(coor[0]), float(coor[1]))
        board.player_blit(p.x, p.y)
        for enemy in board.enemies:
            board.enemy_blit(enemy.x, enemy.y)

        board.show_score()
        board.is_win()
        pygame.display.update()