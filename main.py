import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse Tracker - Red Circle Follows Cursor")

# Clock to control frame rate
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Radius of the circle
RADIUS = 20

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(WHITE)

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw red circle at mouse position
    pygame.draw.circle(screen, RED, (mouse_x, mouse_y), RADIUS)

    # Update the display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
