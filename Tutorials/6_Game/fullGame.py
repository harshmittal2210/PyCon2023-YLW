import pygame
import os
import random
from dinoGame.elements import Track, Dinosaur, SmallCactus
from dinoGame.elements import LargeCactus, Bird, Cloud

pygame.init()
pygame.display.set_caption('Dino Game')

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

alive = True
final_score = 0
while alive:
    SCREEN.fill((255, 255, 255))
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("Press any Key to Start", True, (0, 0, 0))
    
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)

    
    text_score = font.render(f"Score: {final_score}", True, (0, 0, 0))
    score_Rect = text_score.get_rect()
    score_Rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5)

    SCREEN.blit(text, textRect)
    SCREEN.blit(text_score, score_Rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False
        elif event.type == pygame.KEYDOWN:
            ground = Track(SCREEN)
            dino = Dinosaur(SCREEN)
            cloud = Cloud(SCREEN)
            clock = pygame.time.Clock()
            obstacles = []
            points = 0

            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        continue
                
                SCREEN.fill((255,255,255))
                user_input = pygame.key.get_pressed()

                if len(obstacles) == 0:
                    if random.randint(0, 2) == 0:
                        obstacles.append(SmallCactus(SCREEN))
                    elif random.randint(0, 2) == 1:
                        obstacles.append(LargeCactus(SCREEN))
                    elif random.randint(0, 2) == 2:
                        obstacles.append(Bird(SCREEN))
                
                got_hit = False
                for obstacle in obstacles:
                    obstacle.draw()
                    points += obstacle.update(obstacles)
                    if dino.dino_rect.colliderect(obstacle.rect):
                        run = False
                        got_hit = True
                
                if got_hit:
                    final_score = points
                    continue



                ground.draw()
                ground.update()
                dino.update(user_input)
                dino.draw()

                cloud.draw()
                cloud.update()

                text = font.render("Points: " + str(points), True, (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (1000, 40)
                SCREEN.blit(text, textRect)

                clock.tick(30)
                pygame.display.update()
pygame.quit()