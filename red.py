import pygame

def dibujar_red_punteada(pantalla, ancho, alto):
    x_centro = ancho // 2
    largo_segmento = 20
    espaciado = 15

    for y in range(0, alto, largo_segmento + espaciado):
        pygame.draw.rect(pantalla, (255, 255, 255), (x_centro - 1, y, 2, largo_segmento))