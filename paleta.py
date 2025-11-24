import pygame
from constantes import *

class Paleta:
    def __init__(self, x_inicial, y_inicial, velocidad, limite_superior_y, limite_inferior_y, tecla_arriba, tecla_abajo):
        self.x = x_inicial
        self.y = y_inicial
        self.velocidad = velocidad
        self.limite_superior_y = limite_superior_y
        self.limite_inferior_y = limite_inferior_y
        self.tecla_arriba = tecla_arriba
        self.tecla_abajo = tecla_abajo


        self.rect = pygame.Rect(self.x, self.y, ANCHO_PALETA, ALTO_PALETA)
    
    def manejar_input(self):
        """Lee el teclado y ajusta la posición de la paleta"""
        teclas = pygame.key.get_pressed()
        
        if teclas[self.tecla_arriba]:
            self.y -= self.velocidad
        if teclas[self.tecla_abajo]:
            self.y += self.velocidad
            
        # Limites de pantalla de las paletas(no salirse)
        if self.y < self.limite_superior_y:
            self.y = self.limite_superior_y
        if self.y + ALTO_PALETA > self.limite_inferior_y:
            self.y = self.limite_inferior_y - ALTO_PALETA
        
    # Dibuja la figura después del update
    def dibujar(self, surface):
        """Dibuja la paleta como un rectangulo"""
        pygame.draw.rect(surface, COLOR_PALETA, self.rect)
    
    # Se ejecuta en cada frame
    def update(self):
        """Punto central de actualizacion por frame"""
        self.manejar_input()
        self.rect.y = self.y

