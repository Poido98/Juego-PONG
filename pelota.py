import pygame
import random
from paleta import Paleta
from constantes import *

class Pelota:
    def __init__(self, x_inicial, y_inicial, velocidad, ancho_pantalla, alto_pantalla):
        self.x = x_inicial
        self.y = y_inicial
        self.velocidad = velocidad
        self.rect = pygame.Rect(self.x, self.y, ANCHO_PELOTA, ALTO_PELOTA)
        self.dir_x = random.choice([-1, 1])
        self.dir_y = random.choice([-1, 1])
        self.ancho_pantalla = ancho_pantalla
        self.alto_pantalla = alto_pantalla

    def dibujar(self, surface):
        "Dibuja la pelota"
        pygame.draw.rect(surface, COLOR_PELOTA, self.rect)

    # Llamamos a rebotar en bordes para verificar y actualizar si toco en los bordes de la pantalla
    def update(self):
        "Actualiza la posicion de la pelota"
        self.x += self.velocidad * self.dir_x
        self.y += self.velocidad * self.dir_y
        self.rect.x = self.x
        self.rect.y = self.y
        self.rebotar_en_bordes()

    # Rebote en techo y piso de pantalla
    def rebotar_en_bordes(self):
        """Detecta el rebote en el techo y en el piso"""
        if self.rect.top <= 0:
            self.rect.top = 0
            self.y = self.rect.y
            self.dir_y *= -1
        if self.rect.bottom >= self.alto_pantalla:
            self.rect.bottom = self.alto_pantalla
            self.y = self.rect.y
            self.dir_y *= -1
    
    def rebotar_en_paleta(self, paleta):
        """Detecta el rebote en las paletas"""
        # De esta forma cada vez que rebota arriba o abajo de la paleta, desplaza 
        # la pelota un poco para afuera y sigue su recorrido

        if self.rect.colliderect(paleta.rect):
            self.dir_x *= -1
            self.dir_y *= -1

            # Rebote vertical según zona de impacto
            if self.rect.bottom <= paleta.rect.top + 10:
                self.dir_y = -1  # Rebote hacia arriba
            elif self.rect.top >= paleta.rect.bottom - 10:
                self.dir_y = 1   # Rebote hacia abajo
            else:
                self.dir_y *= -1  # Rebote genérico

            # Desplazamiento mínimo para que no se trabe la pelota en la paleta
            if self.dir_x > 0:
                self.rect.left = paleta.rect.right + 1
            else:
                self.rect.right = paleta.rect.left - 1

            self.x = self.rect.x
            self.y = self.rect.y

            return True
        return False

    def fuera_de_pantalla(self):
        "Si se fue afuera de la pantalla"
        if self.rect.right < 0:
            return "izquierda"
        elif self.rect.left > self.ancho_pantalla:
            return "derecha"
        
        return None
    
    def reiniciar(self):
        """Reinicia la pelota al centro en una direccion aleatoria"""
        self.x = self.ancho_pantalla // 2 - ANCHO_PELOTA // 2
        self.y = self.alto_pantalla // 2 - ANCHO_PELOTA // 2
        self.rect.x = self.x
        self.rect.y = self.y
        self.dir_x = random.choice([-1, 1])
        self.dir_y = random.choice([-1, 1])