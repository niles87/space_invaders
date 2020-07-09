import pygame
import os
import random

game_folder = os.path.dirname(__file__)

# initialize game
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(os.path.join(game_folder, 'icon.png'))
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load(os.path.join(game_folder, 'player.png'))
playerX = 370
playerY = 500
playerX_Change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy
enemyImg = pygame.image.load(os.path.join(game_folder, 'enemy.png'))
enemyX = random.randint(0, 800-64)
enemyY = 20
enemyX_Change = 0


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# game loop
running = True
while running:

    screen.fill((0, 15, 90))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keystroke check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change -= 5
            if event.key == pygame.K_RIGHT:
                playerX_Change += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    playerX += playerX_Change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 800-64:
        playerX = 800-64

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
