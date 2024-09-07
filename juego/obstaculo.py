import pygame
import random

class Obstaculo:
    def __init__(self, screen, x, y):
        self.screen = screen
        obstacle_images = [
            pygame.image.load('recursos/obstaculos/obstacle1.png').convert_alpha(),
            pygame.image.load('recursos/obstaculos/obstacle2.png').convert_alpha(),
            pygame.image.load('recursos/obstaculos/obstacle3.png').convert_alpha(),
        ]
        self.image = random.choice(obstacle_images)
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.velocity_x = -1
        self.max_velocity = -10
        self.acceleration = -0.1
    
    def generar_obstaculos(self):
        self.rect.x += self.velocity_x
    
    def dibujar(self):
        self.screen.blit(self.image, self.rect)
    
    def off_screen(self):
        return self.rect.right < 0
    
    def update(self):
        self.generar_obstaculos()
        if self.velocity_x > self.max_velocity:
            self.velocity_x += self.acceleration
