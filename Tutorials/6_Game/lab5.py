import pygame
from dinoGame.elements import Track, Dinosaur, Cloud
from dinoGame.elements import LargeCactus, Bird, SmallCactus

# Initialize Pygame
pygame.init()

SCREEN_HEIGHT = 600  # Enter the window Height
SCREEN_WIDTH = 1100   # Enter the window Width
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


alive = True

while alive:

    SCREEN.fill((255, 255, 255))
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("Press any Key to Start", True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
    SCREEN.blit(text, textRect)

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
            obstacle = None ## Empty Obstacle

            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        continue
                
                ###################################
                if obstacle == None:
                    obstacle = SmallCactus(SCREEN)
                ###################################

                ## Update The Elements
                user_input = pygame.key.get_pressed()
                dino.update(user_input)
                ground.update()
                cloud.update()
                obstacle.update()

                ################

                ### Draw All Layers
                SCREEN.fill((255,255,255))
                ground.draw()
                dino.draw()
                cloud.draw()
                obstacle.draw()

                ##############

                ##### Write code for obstacle update
                #obstacle.rect.x -> X coordinate 
                #obstacle.rect.width -> width
                #print(obstacle.rect.x)

                ###################

                clock.tick(30)
                pygame.display.update()
pygame.quit()