import pygame
import sys

# Initialize Pygame
pygame.init()

########## Make Changes Here##############

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

############## End Code ##################

alive = True

while alive:
    SCREEN.fill((255, 255, 255))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False
        