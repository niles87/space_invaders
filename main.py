import pygame

# initialize game
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
