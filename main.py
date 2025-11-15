import pygame
import sys
from pelota import Pelota
from paleta import Paleta
from red import dibujar_red_punteada

ANCHO = 900
ALTO = 650
VEL_PALETAS = 5
VEL_PELOTA = 3
COLOR_PUNTAJE = (255, 255, 255) # Blanco
puntaje_derecha = 0
puntaje_izquierda = 0


# Inicializamos
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("PONG GAME")
clock = pygame.time.Clock()
COLOR_NEGRO = (0, 0, 0)
fuente_puntaje = pygame.font.SysFont("Arial", 36)

# Creamos la pelota
bola = Pelota(
    image_path = "assets/images/pelota_roja_2.png",
    x_inicial = ANCHO / 2,
    y_inicial = ALTO / 2,
    velocidad = VEL_PELOTA,
    ancho_pantalla = ANCHO,
    alto_pantalla = ALTO
)

# Creamos las paletas
paleta_derecha = Paleta(
    x_inicial= 870,
    y_inicial= 290,
    velocidad= VEL_PALETAS,
    limite_superior_y= 0,
    limite_inferior_y= 650,
    tecla_arriba=pygame.K_UP,
    tecla_abajo= pygame.K_DOWN
)

paleta_izquierda = Paleta(
    x_inicial= 0,
    y_inicial= 290,
    velocidad= VEL_PALETAS,
    limite_superior_y= 0,
    limite_inferior_y= 650,
    tecla_arriba=pygame.K_w,
    tecla_abajo= pygame.K_s
)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(COLOR_NEGRO)

    # Logica del juego
    dibujar_red_punteada(pantalla, ANCHO, ALTO)
    paleta_izquierda.update()
    paleta_derecha.update()
    bola.update()
    bola.dibujar(pantalla) # Pelota
    paleta_izquierda.dibujar(pantalla) # Paleta izquierda
    paleta_derecha.dibujar(pantalla) # Paleta derecha
    bola.rebotar_en_paleta(paleta_izquierda)
    bola.rebotar_en_paleta(paleta_derecha)
    # paleta_izquierda.golpear_pelota(bola)
    # paleta_derecha.golpear_pelota(bola)

    texto_puntaje = fuente_puntaje.render(f"{puntaje_izquierda} : {puntaje_derecha}", True, (COLOR_PUNTAJE))
    pantalla.blit(texto_puntaje, (ANCHO / 2 - texto_puntaje.get_width() // 2, 20))
    

    if bola.fuera_de_pantalla():
        if bola.x < 0:
            puntaje_derecha += 1
        elif bola.x > ANCHO:
            puntaje_izquierda += 1
        bola.reiniciar()
    








    pygame.display.flip()
    clock.tick(60)


