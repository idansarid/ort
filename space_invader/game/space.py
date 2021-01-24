import pygame
from space_invader.game.infra.Board import Board
import random


if __name__ == '__main__':
    board = Board()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.player.playerX_change = -0.1
                if event.key == pygame.K_RIGHT:
                    board.player.playerX_change = 0.1
                if event.key == pygame.K_UP:
                    board.player.playerY_change = -0.1
                if event.key == pygame.K_DOWN:
                    board.player.playerY_change = 0.1
                if event.key == pygame.K_SPACE:
                    if board.bullet.bullet_state == "ready":
                        board.bullet.x = board.player.x
                        board.bullet.y = board.player.y
                        board.fire_bullet(board.bullet.x, board.bullet.y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    board.player.playerX_change = 0
                    board.player.playerY_change = 0

        board.screen.fill((0, 0, 0))
        board.screen.blit(board.background, (0, 0))
        board.player.x += board.player.playerX_change
        board.player.y += board.player.playerY_change
        # boundaries of space ships
        board.player.move()
        for enemy in board.enemies:
            enemy.move()

        # bullet handling
        if board.bullet.y <= 0:
            board.bullet.y = 480
            board.bullet.bullet_state = "ready"
        elif board.bullet.bullet_state == "fire":
            board.fire_bullet(board.bullet.x, board.bullet.y)
            board.bullet.y -= board.bullet.bulletY_change
            # board.bullet_hits_enemy(x2=board.enemy.x, x1=board.bullet.x, y2=board.enemy.y, y1=board.bullet.y)

        for enemy in board.enemies:
            if board.is_collision(x2=enemy.x, x1=board.bullet.x, y2=enemy.y, y1=board.bullet.y):
                board.bullet.y = 480
                board.bullet.bullet_state = "ready"
                board.score += 1
                enemy.x = random.randint(0, 735)
                enemy.y = random.randint(50, 150)
                print(board.score)

        board.player_blit(board.player.x, board.player.y)
        for enemy in board.enemies:
            board.enemy_blit(enemy.x, enemy.y)

        board.show_score()
        pygame.display.update()