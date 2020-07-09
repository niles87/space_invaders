import pygame
import os
import math
import random


game_folder = os.path.dirname(__file__)

# initialize game
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load(os.path.join(
    game_folder, 'imgs/stars_texture.png'))

# background music
pygame.mixer.pre_init()
background_music = pygame.mixer.Sound('sounds/Space_idea.wav')
background_music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(os.path.join(game_folder, 'imgs/icon.png'))
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load(os.path.join(game_folder, 'imgs/player.png'))
playerX = 370
playerY = 500
playerX_Change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Player Attack
bulletImg = pygame.image.load(os.path.join(
    game_folder, 'imgs/player_attack.png'))
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
enemyImg = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(
        os.path.join(game_folder, 'imgs/enemy.png')))
    enemyX.append(random.randint(0, 800-64))
    enemyY.append(60)
    enemyX_Change.append(4)
    enemyY_Change.append(40)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    game_over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (200, 250))

# Collision detection (enemyX enemyY bulletX bulletY)


def isCollision(eX, eY, bX, bY):
    distance = math.sqrt(math.pow(eX - bX, 2) + math.pow(eY - bY, 2))
    if distance < 27:
        return True
    else:
        return False


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
                    bullet_sound = pygame.mixer.Sound('sounds/laser.wav')
                    bullet_sound.play()
                    # get current x coordinate
                    bulletX = playerX
                    player_attack(bulletX, bulletY)
                    pygame.mixer.Sound
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    # player movement
    playerX += playerX_Change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 800-64:
        playerX = 800-64

    # attack movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"
    if bullet_state == "fired":
        player_attack(bulletX, bulletY)
        bulletY -= bulletY_Change

    # enemy movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 500-60:
            for j in range(num_of_enemies):
                enemyY[j] == 2000
            game_over_text()
            break

        enemyX[i] += enemyX_Change[i]

        if enemyX[i] <= 0:
            enemyX_Change[i] = 2.5
            enemyY[i] += enemyY_Change[i]
        elif enemyX[i] >= 800-64:
            enemyX_Change[i] = -2.5
            enemyY[i] += enemyY_Change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion = pygame.mixer.Sound('sounds/explosion.wav')
            explosion.play()
            bulletY = 500
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 800-64)
            enemyY[i] = 20
        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
