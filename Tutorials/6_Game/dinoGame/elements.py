import pygame
import os

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