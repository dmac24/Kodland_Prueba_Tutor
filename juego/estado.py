import pygame
from juego.jugador import Jugador
from juego.obstaculo import Obstaculo

PLAY = 1
END = 0

class Estado:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.jugador = Jugador(screen, 50, height - 300)
        self.obstacles = []
        self.game_state = PLAY
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.background_image = pygame.image.load('recursos/backgroundImg.png').convert()
        self.ground_image = pygame.image.load('recursos/ground.png').convert()
        
        self.game_over_image = pygame.image.load('recursos/gameOver.png').convert_alpha()
        self.restart_image = pygame.image.load('recursos/restart.png').convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (width, height))
        self.ground_image = pygame.transform.scale(self.ground_image, (width, 100))

    def actualizar(self):
        if self.game_state == PLAY:
            self.jugador.mover()
            self.update_obstacles()
            self.spawn_obstacles()
            for obstacle in self.obstacles:
                if self.jugador.rect.colliderect(obstacle.rect):
                    self.jugador.colision()
                    self.game_state = END
            self.score += 1

        elif self.game_state == END:
            self.screen.blit(self.game_over_image, (self.width//2 - 100, self.height//2 - 50))
            self.screen.blit(self.restart_image, (self.width//2 - 50, self.height//2))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.reset()

    def dibujar(self):
        self.screen.blit(self.background_image, (0, 0))
        self.jugador.dibujar()
        for obstaculo in self.obstacles:
            obstaculo.dibujar()
        self.screen.blit(self.ground_image, (0, self.height - 100)) 

        score_text = self.font.render(f'Score: {self.score}', True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))

    def update_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.update()
            if obstacle.off_screen():
                self.obstacles.remove(obstacle)

    def spawn_obstacles(self):
        if len(self.obstacles) < 2:
            self.obstacles.append(Obstaculo(self.screen, self.width, self.height - 95))

    def reset(self):
        self.game_state = PLAY
        self.score = 0
        self.obstacles.clear()
        self.jugador.collided = False