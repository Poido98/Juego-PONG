import pygame
import random
from paleta import Paleta

ANCHO_PELOTA = 20
ALTO_PELOTA = 20
COLOR_PELOTA = (255, 0, 0)

class Pelota:
    def __init__(self, image_path, x_inicial, y_inicial, velocidad, ancho_pantalla, alto_pantalla):
        # self.image = pygame.image.load(image_path) 
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
        if self.rect.bottom >= self.alto_pantalla:
            self.rect.bottom = self.alto_pantalla
            self.y = self.rect.y
            self.dir_y *= -1
    
    def rebotar_en_paleta(self, paleta):
        """Detecta el rebote en las paletas"""
        # if self.rect.colliderect(paleta.rect):
        #     self.dir_x *= -1
        #     self.dir_y *= -1

        #     # Detecta si rebota arriba y abajo de las paletas
        #     if self.rect.bottom <= paleta.rect.top + 10: # Rebote hacia arriba
        #         self.dir_y *= -1
            
        #     elif self.rect.top >= paleta.rect.bottom - 10: # Rebote hacia abajo
        #         self.dir_y *= 1
                
        #     else:
        #         self.dir_y *= -1
                
        #     paleta.x = paleta.rect.x
        #     paleta.y = paleta.rect.y

        # ---------------------------------------------------------------------------

        # La unica forma de arreglar el rebote es con el rect.centery, que calcula dónde está el centro vertical de un objeto

        # if self.rect.colliderect(paleta.rect):
        #     self.dir_x *= -1  # Rebote horizontal

        #     offset = self.rect.centery - paleta.rect.centery # Mide la distancia desde el centro de la pelota y el centro de la paleta

        #     if offset < -30:
        #         self.dir_y = -1 # Golpe en parte superior, rebota para arriba
        #     elif offset > 30:
        #         self.dir_y = 1 # Golpe en parte inferior, rebota para abajo
        #     else:
        #         pass # Mantiene la direccion vertical

        # ----------------------------------------------------------------------------

        # De esta forma cada vez que rebota arriba o abajo de la paleta, como que desplaza 
        # la pelota un poco para afuera y sigue su recorrido

        if self.rect.colliderect(paleta.rect):
            self.dir_x *= -1
            self.dir_y *= -1

            # Rebote vertical según zona de impacto
            if self.rect.bottom <= paleta.rect.top + 10:
                self.dir_y = -1  # rebote hacia arriba
            elif self.rect.top >= paleta.rect.bottom - 10:
                self.dir_y = 1   # rebote hacia abajo
            else:
                self.dir_y *= -1  # rebote genérico

            # Desplazamiento mínimo
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