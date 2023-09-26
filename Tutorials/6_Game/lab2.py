import pygame
import sys

# Initialize Pygame
pygame.init()

SCREEN_HEIGHT = 600  # Enter the window Height
SCREEN_WIDTH = 1100   # Enter the window Width
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


alive = True

while alive:

    ########## Make Changes Here##############
    SCREEN.fill((__, __, __))
    ############## End Code ##################

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False
        