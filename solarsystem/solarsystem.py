# You can use the Pygame library to create a simple solar system animation
import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Solar System Animation")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Constants
sun_radius = 30
earth_radius = 10
moon_radius = 5
earth_distance = 100
moon_distance = 20

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Draw sun
    pygame.draw.circle(screen, YELLOW, (400, 300), sun_radius)

    # Draw earth
    earth_x = 400 + earth_distance * math.cos(pygame.time.get_ticks() / 1000)
    earth_y = 300 + earth_distance * math.sin(pygame.time.get_ticks() / 1000)
    pygame.draw.circle(screen, BLUE, (int(earth_x), int(earth_y)), earth_radius)

    # Draw moon
    moon_x = earth_x + moon_distance * math.cos(pygame.time.get_ticks() / 500)
    moon_y = earth_y + moon_distance * math.sin(pygame.time.get_ticks() / 500)
    pygame.draw.circle(screen, RED, (int(moon_x), int(moon_y)), moon_radius)

    pygame.display.flip()