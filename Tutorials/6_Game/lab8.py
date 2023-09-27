##########################################
"""
Lab:8 Objectives
- Have Different Obstacles
"""
##########################################
import pygame
from dinoGame.elements import Track, Dinosaur, Cloud
from dinoGame.elements import LargeCactus, Bird, SmallCactus

# Initialize Pygame
pygame.init()

SCREEN_HEIGHT = 600  # Enter the window Height
SCREEN_WIDTH = 1100   # Enter the window Width
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


alive = True

total_score = 0

while alive:

    SCREEN.fill((255, 255, 255))
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("Press any Key to Start", True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
    SCREEN.blit(text, textRect)

    text_score = font.render(f"Score: {total_score}", True, (0, 0, 0))
    score_Rect = text_score.get_rect()
    score_Rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5)
    SCREEN.blit(text_score, score_Rect)

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
            obstacle = None

            game_score = 0

            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        continue
                ##########Have Different Obstacles#########
                if obstacle == None:
                    obstacle = LargeCactus(SCREEN)
                ###########################################

                ## Update The Elements
                user_input = pygame.key.get_pressed()
                dino.update(user_input)
                ground.update()
                cloud.update()
                obstacle.update()

                ### Draw All Layers
                SCREEN.fill((255,255,255))
                ground.draw()
                dino.draw()
                cloud.draw()
                obstacle.draw()

                if dino.dino_rect.colliderect(obstacle.rect):
                    total_score  = game_score
                    break

                if obstacle.rect.x <= -obstacle.rect.width:
                    obstacle = None
                    game_score += 1

                text = font.render("Points: " + str(game_score), True, (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
                SCREEN.blit(text, textRect)

                clock.tick(30)
                pygame.display.update()
pygame.quit()