import sys
import pygame
import random

# Initialize Pygame
pygame.init()

# --------------- General content-----------------------
HEIGHT = 700
WIDTH = 500
color_red = (255, 0, 0)
color_blue = (0, 0, 255)
color_dark = (0, 0, 0)
color_white = (255, 255, 255)


# Constants for the home screen--------
START_SCREEN = 0
GAME_SCREEN = 1
current_screen = START_SCREEN

start_button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - 25, 150, 50)
button_clicked = False

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

# Enemy positions and speeds
enemies = []
enemy_speeds = []
num_enemies = 1  # Default to 2 enemies

for i in range(2):  # Create two enemies
    enemies.append([random.randint(0, WIDTH - enemy_size), 0])
    #We start the first slow lap
    enemy_speeds.append(random.randint(10, 20))

# ---------------Game screen---------------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

# We define a clock
clock = pygame.time.Clock()

#----------------Funtions--------------------------
def show_start_screen():
    global current_screen, num_enemies

    # Button to start the game
    start_button_rect = pygame.Rect(WIDTH // 2 - 75, 200, 150, 50)
    pygame.draw.rect(screen, color_blue, start_button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Start", True, color_white)
    text_rect = text.get_rect()
    text_rect.center = start_button_rect.center
    screen.blit(text, text_rect)

    # Check if the home button was clicked
    if start_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, color_white, start_button_rect, 2)
        if pygame.mouse.get_pressed()[0] and current_screen == START_SCREEN:
            current_screen = GAME_SCREEN

    # Buttons to select the number of enemies
    btn1enemy = pygame.Rect(WIDTH // 4 - 50, HEIGHT // 2 + 50, 130, 50)
    btn2enemy = pygame.Rect(3 * WIDTH // 4 - 50, HEIGHT // 2 + 50, 130, 50)

    pygame.draw.rect(screen, color_blue, btn1enemy)
    pygame.draw.rect(screen, color_blue, btn2enemy)

    font = pygame.font.Font(None, 36)
    text1 = font.render("1 Enemy", True, color_white)
    text2 = font.render("2 Enemies", True, color_white)

    text_rect1 = text1.get_rect()
    text_rect2 = text2.get_rect()

    text_rect1.center = btn1enemy.center
    text_rect2.center = btn2enemy.center

    screen.blit(text1, text_rect1)
    screen.blit(text2, text_rect2)

    if btn1enemy.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, color_white, btn1enemy, 2)
        if pygame.mouse.get_pressed()[0] and current_screen == START_SCREEN:
            num_enemies = 1
    elif btn2enemy.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, color_white, btn2enemy, 2)
        if pygame.mouse.get_pressed()[0] and current_screen == START_SCREEN:
            num_enemies = 2

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
        if button_clicked:
            current_screen = GAME_SCREEN

    if current_screen == GAME_SCREEN:

#--------------Player movement---------------------
        # If the user presses a key, check which key was pressed
        if event.type == pygame.KEYDOWN:
            # Coordinate X
            x = player_pos[0]
            if event.key == pygame.K_LEFT:
                x -= player_size

            if event.key == pygame.K_RIGHT:
                x += player_size

        #Verify that the player does not go beyond the limits of the screen-------------------
        
            if x < 0: # Do not allow it to exit to the left
                x = 0
            elif x > WIDTH - player_size:  # Do not allow it to exit to the right
                x = WIDTH - player_size

            # The player's position is assigned to the X coordinate
            player_pos[0] = x

    # We restart the screen to create a motion effect
        screen.fill(color_dark)
        for i in range(num_enemies):
            if enemies[i][1] >= 0 and enemies[i][1] < HEIGHT:
                enemies[i][1] += enemy_speeds[i]
            else:
                enemies[i] = [random.randint(0, WIDTH - enemy_size), 0]
                enemy_speeds[i] = random.randint(2, 5)
            pygame.draw.rect(screen, color_red, (enemies[i][0], enemies[i][1], enemy_size, enemy_size))
            if detect_collision(player_pos, enemies[i]):
                game_over = True

        pygame.draw.rect(screen, color_blue, (player_pos[0], player_pos[1], player_size, player_size))
        clock.tick(30)
        pygame.display.update()


        # We limit the Fhz
        clock.tick(30)
        pygame.display.update()

# Finish Pygame
pygame.quit()