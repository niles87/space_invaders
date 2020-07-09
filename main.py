import pygame
import os
import random

game_folder = os.path.dirname(__file__)

# initialize game
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load(os.path.join(game_folder, 'stars_texture.png'))

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


# Player Attack
bulletImg = pygame.image.load(os.path.join(game_folder, 'player_attack.png'))
bulletX = 0
bulletY = playerY
bulletX_Change = 0
bulletY_Change = 7
# bullet states ready and fired
bullet_state = "ready"


def player_attack(x, y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bulletImg, (x + 27, y + 5))


# Enemy
enemyImg = pygame.image.load(os.path.join(game_folder, 'enemy.png'))
enemyX = random.randint(0, 800-64)
enemyY = 20
enemyX_Change = 2.5
enemyY_Change = 40


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# game loop
running = True
while running:

    screen.fill((0, 15, 90))
    # backgound image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keystroke check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change -= 5
            if event.key == pygame.K_RIGHT:
                playerX_Change += 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # get current x coordinate
                    bulletX = playerX
                    player_attack(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    playerX += playerX_Change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 800-64:
        playerX = 800-64

    enemyX += enemyX_Change

    if enemyX <= 0:
        enemyX_Change = 2.5
        enemyY += enemyY_Change
    elif enemyX >= 800-64:
        enemyX_Change = -2.5
        enemyY += enemyY_Change

    # attack movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"
    if bullet_state == "fired":
        player_attack(bulletX, bulletY)
        bulletY -= bulletY_Change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
