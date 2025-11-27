import pygame
import sys
from constantes import *

def pedir_nombres(pantalla, fuente):
    """La funcion donde pedimos los nombres de los jugadores"""
    fuente_input = pygame.font.Font(font_juego, 30)
    clock = pygame.time.Clock()

    # Almacenamos los nombres en una lista
    nombres = []

    # Con el unicode se escribe la tecla que el jugador escribio, necesario para escribir el nombre
    for i in range(2):
        nombre = ""
        escribiendo = True
        while escribiendo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        nombres.append(nombre)
                        escribiendo = False
                    else:
                        nombre += event.unicode

            pantalla.fill(COLOR_NEGRO)

            # Mensaje arriba 
            if i == 0:
                mensaje = f"Nombre del jugador {i + 1} (izquierda)"
            else:
                mensaje = f"Nombre del jugador {i + 1} (derecha)"
            texto_titulo = fuente.render(mensaje, True, COLOR_BLANCO)
            pantalla.blit(texto_titulo, texto_titulo.get_rect(center=(ANCHO // 2, ALTO // 2 - 100)))

            # Texto del jugador
            texto_render = fuente_input.render(nombre, True, COLOR_BLANCO)
            pantalla.blit(texto_render, (ANCHO//2 - 140, ALTO//2))

            # Actualizamos la pantalla
            pygame.display.flip()
            clock.tick(60)

    return nombres[0], nombres[1]


