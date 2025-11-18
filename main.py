import pygame
import sys
from pelota import Pelota
from paleta import Paleta
from red import dibujar_red_punteada
from botones import Boton

ANCHO = 900
ALTO = 650
VEL_PALETAS = 5
VEL_PELOTA = 3
COLOR_PUNTAJE = (255, 255, 255) # Blanco
img_fondo = pygame.image.load("assets\images\menu_sin_titulo.png")
img_fondo_opciones = pygame.image.load("assets\images\Background.png")
font_juego = "fonts\juego_font.ttf"

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))


def jugar():
    pygame.display.set_caption("PONG GAME")
    clock = pygame.time.Clock()
    COLOR_NEGRO = (0, 0, 0)
    fuente_puntaje = pygame.font.SysFont("Arial", 90)

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

    puntaje_derecha = 0
    puntaje_izquierda = 0

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
        if bola.rebotar_en_paleta(paleta_izquierda) or bola.rebotar_en_paleta(paleta_derecha):
            bola.velocidad += 0.5

        texto_puntaje = fuente_puntaje.render(f"{puntaje_izquierda}  {puntaje_derecha}", True, (COLOR_PUNTAJE))
        pantalla.blit(texto_puntaje, (ANCHO / 2 - texto_puntaje.get_width() // 2, 20))
        

        if bola.fuera_de_pantalla():
            if bola.x < 0:
                puntaje_derecha += 1
            elif bola.x > ANCHO:
                puntaje_izquierda += 1
            bola.reiniciar()

        pygame.display.flip()
        clock.tick(60)
            

        

        # PLAY_BACK = Boton(image=None, pos=(640, 460), 
        #                     text_input="ATRAS", font=pygame.font.Font(font_juego, 75), color_base="White", color_mouse_arriba="Green")

        # PLAY_BACK.cambiar_color(pos_mouse)
        # PLAY_BACK.update(pantalla)

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if PLAY_BACK.chequear_input(pos_mouse):
        #             menu_principal()

        # pygame.display.update()

def ultimas_partidas():
    while True:
        pos_mouse = pygame.mouse.get_pos()

        pantalla.fill("white")

        OPTIONS_TEXT = pygame.font.Font(font_juego, 20).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(ANCHO, ALTO - 150))
        pantalla.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Boton(image=pygame.image.load("assets\images\Jugar Rect.png"), pos=(ANCHO / 2, ALTO / 2 + 100), text_input="ATRAS", 
                            font=pygame.font.Font(font_juego, 20), color_base="Black", color_mouse_arriba="Green")

        OPTIONS_BACK.cambiar_color(pos_mouse)
        OPTIONS_BACK.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(pos_mouse):
                    menu_principal()

        pygame.display.update()


def menu_principal():
    while True:

        pantalla.blit(img_fondo, (0, 0))

        pygame.display.set_caption("Menu")

        pos_mouse = pygame.mouse.get_pos()

        TITULO_MENU = pygame.font.Font(font_juego, 70).render("PONG GAME", True, (255, 255, 0))
        MENU_RECT = TITULO_MENU.get_rect(center=(ANCHO / 2, 60))

        BOTON_JUGAR = Boton(image=pygame.image.load("assets\images\Jugar Rect.png"), pos=(ANCHO / 2, ALTO / 2 - 120), text_input="JUGAR",
                            font=pygame.font.Font(font_juego, 20), color_base= (255, 255, 0), color_mouse_arriba=(255, 255, 255))
        
        BOTON_PUNTAJE = Boton(image=pygame.image.load("assets\images\Jugar Rect.png"), pos=(ANCHO / 2, ALTO / 2), text_input="PUNTAJES",
                            font=pygame.font.Font(font_juego, 20), color_base= (255, 255, 0), color_mouse_arriba=(255, 255, 255))
        
        BOTON_SALIR = Boton(image=pygame.image.load("assets\images\Jugar Rect.png"), pos=(ANCHO / 2, ALTO / 2 + 120), text_input="SALIR",
                            font=pygame.font.Font(font_juego, 20), color_base= (255, 255, 0), color_mouse_arriba=(255, 255, 255))
        
        pantalla.blit(TITULO_MENU, MENU_RECT)

        for boton in [BOTON_JUGAR, BOTON_PUNTAJE, BOTON_SALIR]:
            boton.cambiar_color(pos_mouse)
            boton.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_JUGAR.chequear_input(pos_mouse):
                    jugar()
                if BOTON_PUNTAJE.chequear_input(pos_mouse):
                    ultimas_partidas()
                if BOTON_SALIR.chequear_input(pos_mouse):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()

menu_principal()


