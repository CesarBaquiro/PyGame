import sys
import pygame
import random

# --------------- General content-----------------------
HEIGHT = 700
WIDTH = 500
color_red = (255, 0, 0)
color_blue = (0, 0, 255)
color_dark = (0, 0, 0)

# ---------------- Player content-------------------------

# Player size-----------
player_size = 50

# Player position -------------
# Width: We divide the width by 2 to find the exact half
# Height: We subtract the size of the player, 2 times from the height, to leave a margin
player_pos = [WIDTH/2, HEIGHT-player_size*2]

# ---------------- Enemy content-------------------------

# Enemy size-----------
enemy_size = 50
# Enemy position -------------
# We subtract the size of the enemy to leave a margin
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]

# ---------------Game screen---------------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

# We define a clock
clock = pygame.time.Clock()

# ----------------Collision system------------------


def detect_collision(player_pos, enemy_pos):
    # Player axis X
    px = player_pos[0]
    # Player axis Y
    py = player_pos[1]

    # Enemy axis X
    ex = enemy_pos[0]
    # Enemy axis Y
    ey = enemy_pos[1]

    if (ex >= px and ex < (px + player_size)) or (px >= ex and px < (ex + enemy_size)):
        if (ey >= py and ey < (py + player_size)) or (py >= ey and py < (ey + enemy_size)):
            return True
    return False

# ---------------Game cycle---------------------


while not game_over:
    for event in pygame.event.get():

        # If the user presses exit, close the window
        if event.type == pygame.QUIT:
            sys.exit()

        # If the user presses a key, check which key was pressed
        if event.type == pygame.KEYDOWN:
            # Coordinate X
            x = player_pos[0]
            if event.key == pygame.K_LEFT:
                x -= player_size

            if event.key == pygame.K_RIGHT:
                x += player_size

            # The player's position is assigned to the X coordinate
            player_pos[0] = x

    # We restart the screen to create a motion effect
    screen.fill(color_dark)

    if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
        enemy_pos[1] += 20
    else:
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        enemy_pos[1] = 0

    # Collisions
    if detect_collision(player_pos, enemy_pos):
        game_over = True

    # We draw our player
    pygame.draw.rect(screen, color_blue,
                     (player_pos[0], player_pos[1], player_size, player_size))

    # We draw our enemy
    pygame.draw.rect(screen, color_red,
                     (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    # We limit the Fhz
    clock.tick(30)
    pygame.display.update()
