import pygame
import os
import random
from dinoGame.elements import Track, Dinosaur

pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

alive = True

while alive:
    SCREEN.fill((255, 255, 255))
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("Press any Key to Start", True, (0, 0, 0))
    
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    SCREEN.blit(text, textRect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False
        elif event.type == pygame.KEYDOWN:
            ground = Track(SCREEN)
            dino = Dinosaur(SCREEN)
            clock = pygame.time.Clock()
            obstacles = []

            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        continue
                
                SCREEN.fill((255,255,255))
                user_input = pygame.key.get_pressed()

                


                ground.draw()
                dino.update(user_input)
                dino.draw()
                clock.tick(30)
                pygame.display.update()