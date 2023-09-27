##########################################
"""
Lab:1 Objectives
- Create game screen with custom size
"""
##########################################

import pygame

# Initialize Pygame
pygame.init()

########## Make Changes Here##############

SCREEN_HEIGHT =   # Enter the window Height (>400)
SCREEN_WIDTH =    # Enter the window Width (>400)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

############## End Code ##################

alive = True

while alive:
    SCREEN.fill((255, 255, 255))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False
pygame.quit()