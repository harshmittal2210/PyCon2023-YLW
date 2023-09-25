import pygame
import os
import random

file_folder = os.path.join(os.path.abspath(__file__).rsplit("/", 1)[0])


class Track():
    def __init__(self, screen:pygame.Surface, game_speed=20) -> None:
        self.image = pygame.image.load(os.path.join(file_folder, "img", "Track.png"))
        self.image_width = self.image.get_width()
        self.x = 0
        self.y = 380
        self.screen:pygame.Surface = screen
        self.game_speed = game_speed

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.screen.blit(self.image, (self.image_width + self.x, self.y))
        if self.x <= -self.image_width:
            self.screen.blit(self.image, (self.image_width + self.x, self.y))
            self.x = 0
        self.x -= self.game_speed

class Dinosaur():
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5
    def __init__(self, screen) -> None:
        self.run_img = [pygame.image.load(os.path.join(file_folder, "img", "DinoRun1.png")),
                        pygame.image.load(os.path.join(file_folder, "img", "DinoRun2.png"))]
        self.jump_img = pygame.image.load(os.path.join(file_folder, "img", "DinoJump.png"))
        self.duck_img = [pygame.image.load(os.path.join(file_folder, "img", "DinoDuck1.png")),
                        pygame.image.load(os.path.join(file_folder, "img", "DinoDuck2.png"))]
        
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.screen = screen
    
    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self):
        self.screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Obstacle:
    def __init__(self, screen, image, type, game_speed=20):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.screen:pygame.Surface = screen
        self.rect.x = self.screen.get_width()
        self.game_speed = game_speed

    def update(self, obstacles):
        self.rect.x -= self.game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
            return 1
        return 0

    def draw(self):
        self.screen.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, screen):
        self.type = random.randint(0, 2)
        image = [pygame.image.load(os.path.join(file_folder, "img", "SmallCactus1.png")),
                pygame.image.load(os.path.join(file_folder, "img", "SmallCactus2.png")),
                pygame.image.load(os.path.join(file_folder, "img", "SmallCactus3.png"))]
        super().__init__(screen, image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, screen):
        self.type = random.randint(0, 2)
        image = [pygame.image.load(os.path.join(file_folder, "img", "LargeCactus1.png")),
                pygame.image.load(os.path.join(file_folder, "img", "LargeCactus2.png")),
                pygame.image.load(os.path.join(file_folder, "img", "LargeCactus3.png"))]
        super().__init__(screen, image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, screen):
        self.type = 0
        image = [pygame.image.load(os.path.join(file_folder, "img", "Bird1.png")),
                pygame.image.load(os.path.join(file_folder, "img", "Bird2.png"))]
        super().__init__(screen, image, self.type)
        self.rect.y = 250
        self.index = 0
        

    def draw(self):
        if self.index >= 9:
            self.index = 0
        self.screen.blit(self.image[self.index//5], self.rect)
        self.index += 1

class Cloud:
    def __init__(self, screen, game_speed=20):
        self.screen:pygame.Surface = screen
        self.x = self.screen.get_width() + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = pygame.image.load(os.path.join(file_folder, "img", "Cloud.png"))
        self.width = self.image.get_width()
        self.game_speed = game_speed

    def update(self):
        self.x -= self.game_speed
        if self.x < -self.width:
            self.x = self.screen.get_width() + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))