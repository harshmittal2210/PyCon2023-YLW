import pygame
from dinoGame.elements import Track, Dinosaur, Cloud

# Initialize Pygame
pygame.init()

SCREEN_HEIGHT = 600  # Enter the window Height
SCREEN_WIDTH = 1100   # Enter the window Width
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


alive = True

while alive:

    SCREEN.fill((255, 255, 255))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False
        elif event.type == pygame.KEYDOWN:
            ## Start Game
            ground = Track(SCREEN)
            dino = Dinosaur(SCREEN)
            cloud = Cloud(SCREEN)
            clock = pygame.time.Clock()

            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        continue

                ## Update The Elements
                user_input = pygame.key.get_pressed()
                dino.update(user_input)
                ground.update()

                ################

                ### Draw All Layers
                SCREEN.fill((255,255,255))
                ground.draw()

                ##############End

                clock.tick(30)
                pygame.display.update()
pygame.quit()