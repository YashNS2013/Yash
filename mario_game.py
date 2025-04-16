import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Mario character
mario = pygame.Rect(50, 500, 50, 50)

# Ground
ground = pygame.Rect(0, 550, SCREEN_WIDTH, 50)

# Gravity and jump variables
gravity = 0.5
mario_y_velocity = 0
is_jumping = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get key states
    keys = pygame.key.get_pressed()

    # Mario movement
    if keys[pygame.K_LEFT]:
        mario.x -= 5
    if keys[pygame.K_RIGHT]:
        mario.x += 5
    if keys[pygame.K_SPACE] and not is_jumping:
        mario_y_velocity = -10
        is_jumping = True

    # Apply gravity
    mario_y_velocity += gravity
    mario.y += mario_y_velocity

    # Check for collision with the ground
    if mario.colliderect(ground):
        mario.y = ground.y - mario.height
        mario_y_velocity = 0
        is_jumping = False

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, mario)  # Draw Mario
    pygame.draw.rect(screen, BLACK, ground)  # Draw ground

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)