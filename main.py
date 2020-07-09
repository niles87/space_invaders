import pygame
import os

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
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 15, 90))

    player()
    pygame.display.update()
