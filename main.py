import pygame
import sys
from juego.jugador import Jugador
from juego.obstaculo import Obstaculo
from juego.estado import Estado

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Trex Corredor')

estado = Estado(pantalla, 800, 600)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    estado.actualizar()

    estado.dibujar()
    pygame.display.flip()