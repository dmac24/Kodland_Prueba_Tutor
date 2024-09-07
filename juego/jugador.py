import pygame

class Jugador:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.images = [
            pygame.image.load('recursos/jugador/trex_1.png').convert_alpha(),
            pygame.image.load('recursos/jugador/trex_2.png').convert_alpha(),
            pygame.image.load('recursos/jugador/trex_3.png').convert_alpha()
        ]
        self.collided_image = pygame.image.load('recursos/jugador/trex_collided.png').convert_alpha()
        self.images = [pygame.transform.scale(img, (100, 100)) for img in self.images]
        self.collided_image = pygame.transform.scale(self.collided_image, (100, 100))
        
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.velocity_y = 0
        self.gravity = 0.8
        self.jump_speed = -10
        self.collided = False
        self.jump_sound = pygame.mixer.Sound('recursos/sonidos/jump.wav')
        self.collided_sound = pygame.mixer.Sound('recursos/sonidos/collided.wav')
        self.animation_speed = 0.1
        self.animation_time = 0

    def mover(self):
        if not self.collided:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
                self.velocity_y = self.jump_speed
                self.jump_sound.play()

            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y
            if self.rect.bottom >= 500:
                self.rect.bottom = 500
                self.velocity_y = 0
        self.animation_time += self.animation_speed
        if self.animation_time >= len(self.images):
            self.animation_time = 0
        self.current_image = int(self.animation_time)
        self.image = self.images[self.current_image]

    def dibujar(self):
        self.screen.blit(self.image, self.rect)

    def colision(self):
        self.image = self.collided_image
        self.collided = True
        self.collided_sound.play()
