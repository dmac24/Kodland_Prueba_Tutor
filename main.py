import pygame
import sys
from juego.jugador import Jugador
from juego.obstaculo import Obstaculo
from juego.estado import Estado

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Trex Corredora Color')

# Inicializar objetos del juego
jugador = Jugador()
obstaculo = Obstaculo()
estado = Estado()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Lógica
    jugador.mover()
    obstaculo.generar_obstaculos()
    estado.actualizar()

    # Render
    pantalla.fill((255, 255, 255))
    jugador.dibujar(pantalla)
    obstaculo.dibujar(pantalla)
    pygame.display.flip()