import pygame
import random

ANCHO_PELOTA = 20
ALTO_PELOTA = 20
COLOR_PELOTA = (255, 0, 0)

class Pelota:
    def __init__(self, image_path, x_inicial, y_inicial, velocidad):
        # self.image = pygame.image.load(image_path) 
        self.x = x_inicial
        self.y = y_inicial
        self.velocidad = velocidad
        self.rect = pygame.Rect(self.x, self.y, ANCHO_PELOTA, ALTO_PELOTA)
        self.dir_x = random.choice([-1, 1])
        self.dir_y = random.choice([-1, 1])

    def dibujar(self, surface):
        "Dibuja la pelota"
        pygame.draw.rect(surface, COLOR_PELOTA, self.rect)
        # surface.blit(self.image, (self.x, self.y))
        # pygame.draw.circle(surface, COLOR_PELOTA, (self.x, self.y), 30)

    def update(self):
        "Actualiza la posicion de la pelota"
        self.x += self.velocidad * self.dir_x
        self.y += self.velocidad * self.dir_y
        self.rect.x = self.x
        self.rect.y = self.y
        self.rebotar_en_bordes()
        
        
    # Capaz se puede hacer algo aca para que rebote directo cuando entre en contacto con la paleta 


    # Rebote en techo y piso de pantalla (ver si conviene hacer aca o en el main como el de la nave)
    def rebotar_en_bordes(self):
        """Detecta el rebote en el techo y en el piso"""
        if self.rect.top <= 0:
            self.rect.top = 0
            self.y = self.rect.y
            self.dir_y *= -1
        if self.rect.bottom >= 650:
            self.rect.bottom = 650
            self.y = self.rect.y
            self.dir_y *= -1

    def fuera_de_pantalla(self):
        "Si se fue afuera de la pantalla"
        if self.rect.right < 0:
            return "izquierda"
        elif self.rect.left > 900:
            return "derecha"
        
        return None
    
    def reiniciar(self):
        """Reinicia la pelota al centro en una direccion aleatoria"""
        self.x = 900 // 2 - ANCHO_PELOTA // 2
        self.y = 650 // 2 - ANCHO_PELOTA // 2
        self.rect.x = self.x
        self.rect.y = self.y
        self.dir_x = random.choice([-1, 1])
        self.dir_y = random.choice([-1, 1])