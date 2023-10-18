import sys
import pygame
import random

# Inicializar Pygame
pygame.init()

# --------------- General content-----------------------
HEIGHT = 700
WIDTH = 500
color_red = (255, 0, 0)
color_blue = (0, 0, 255)
color_dark = (0, 0, 0)
color_white = (255, 255, 255)


# Constantes para la pantalla de inicio--------
START_SCREEN = 0
GAME_SCREEN = 1
current_screen = START_SCREEN

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

#----------------Funtions--------------------------
def show_start_screen():
    global current_screen
    screen.fill(color_dark)
    font = pygame.font.Font(None, 36)
    text = font.render("Press SPACE to Start", True, color_white)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, text_rect)
    pygame.display.update()

  



# Collision system------------------

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

show_start_screen()
        
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if current_screen == START_SCREEN:
        show_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                current_screen = GAME_SCREEN

    if current_screen == GAME_SCREEN:

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

# Finalizar Pygame
pygame.quit()