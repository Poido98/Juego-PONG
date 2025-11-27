import pygame
import sys
from pelota import Pelota
from paleta import Paleta
from red import dibujar_red_punteada
from botones import Boton
from constantes import *
from ingreso_nombres import pedir_nombres


pygame.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))


def juego_terminado(pantalla, fuente, ganador):
    """La pantalla que aparece una vez que finalizamos el juego"""

    # Limpiamos la pantalla
    pantalla.fill(COLOR_AZUL_OSCURO)

    # Creamos los distintos textos
    texto_terminado = fuente.render("JUEGO TERMINADO", True, COLOR_AMARILLO)
    rect = texto_terminado.get_rect(center=(ANCHO // 2, ALTO // 2 - 100))
    pantalla.blit(texto_terminado, rect)

    texto_ganador = fuente.render(f"{ganador} ha ganado", True, COLOR_AMARILLO)
    rect = texto_ganador.get_rect(center=(ANCHO // 2, ALTO // 2 - 40))
    pantalla.blit(texto_ganador, rect)
    
    texto_salir = fuente.render("Presione ESC para salir", True, COLOR_BLANCO)
    rect = texto_salir.get_rect(center=(ANCHO // 2, ALTO // 2 + 20))
    pantalla.blit(texto_salir, rect)

    texto_continuar = fuente.render("Presione ESPACIO para volver al menu", True, COLOR_BLANCO)
    rect = texto_continuar.get_rect(center=(ANCHO // 2, ALTO // 2 + 80))
    pantalla.blit(texto_continuar, rect)

    pygame.display.flip()
    
    # Esperamos que el usuario presione la BARRA o ESC
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                menu_principal()


def jugar():
    pygame.display.set_caption("PONG GAME")
    clock = pygame.time.Clock()
    fuente_puntaje = pygame.font.SysFont("Arial", 90)
    fuente_nombres = pygame.font.Font(font_juego, 25)


    # Creamos la pelota
    bola = Pelota(
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

    # Cargamos los nombres de los jugadores
    nombre_izquierda, nombre_derecha = pedir_nombres(pantalla, pygame.font.Font(font_juego, 22))

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

        # Aumentamos la velocidad con cada golpe de la paleta
        if bola.rebotar_en_paleta(paleta_izquierda) or bola.rebotar_en_paleta(paleta_derecha):
            bola.velocidad += 0.5

        # Dibujamos el puntaje
        texto_puntaje = fuente_puntaje.render(f"{puntaje_izquierda}  {puntaje_derecha}", True, (COLOR_BLANCO))
        pantalla.blit(texto_puntaje, (ANCHO / 2 - texto_puntaje.get_width() // 2, 23))

        # Dibujamos los nombres
        texto_jug_izquierda = fuente_nombres.render(nombre_izquierda, True, COLOR_BLANCO)
        pantalla.blit(texto_jug_izquierda, (ANCHO // 2 - 350, 20))
        texto_jug_derecha = fuente_nombres.render(nombre_derecha, True, COLOR_BLANCO)
        pantalla.blit(texto_jug_derecha, (ANCHO // 2 + 200, 20))

        # Si se va fuera de pantalla manejamos el puntaje
        if bola.fuera_de_pantalla():
            if bola.x < 0:
                puntaje_derecha += 1
            elif bola.x > ANCHO:
                puntaje_izquierda += 1
            bola.reiniciar()
            bola.velocidad = VEL_PELOTA

            # Puntaje maximo 
            if puntaje_derecha >= 10:
                juego_terminado(pantalla, pygame.font.Font(font_juego, 22), nombre_derecha)
            elif puntaje_izquierda >= 10:
                juego_terminado(pantalla, pygame.font.Font(font_juego, 22), nombre_izquierda)

        pygame.display.flip()
        clock.tick(60)
            

def menu_principal():
    """El menu principal del juego"""

    pygame.mixer.init()
    pygame.mixer.music.load("sound\sonido_arcade.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    sonido_activo = True

    # Obtenemos el rect de las imagenes del sonido
    rect_sonido = img_sonido.get_rect(topleft=(780, 20))
    rect_sonido_mute = img_sonido_mute.get_rect(topleft=(780, 20))

    while True:

        pantalla.blit(img_fondo, (0, 0))

        pygame.display.set_caption("Menu")
        # Obtenemos la posicion del mouse
        pos_mouse = pygame.mouse.get_pos()

        # Creanos el titulo del menu principal
        TITULO_MENU = pygame.font.Font(font_juego, 70).render("PONG GAME", True, COLOR_AMARILLO)
        MENU_RECT = TITULO_MENU.get_rect(center=(ANCHO / 2, 60))

        # Creamos los botones
        BOTON_JUGAR = Boton(image=pygame.image.load("assets\images\img_fondo_boton.png"), pos=(ANCHO / 2, ALTO / 2 - 60), texto_input="JUGAR",
                            font=pygame.font.Font(font_juego, 30), color_base= COLOR_AMARILLO, color_mouse_arriba=COLOR_AZUL_OSCURO)
        
        BOTON_SALIR = Boton(image=pygame.image.load("assets\images\img_fondo_boton.png"), pos=(ANCHO / 2, ALTO / 2 + 60), texto_input="SALIR",
                            font=pygame.font.Font(font_juego, 30), color_base= COLOR_AMARILLO, color_mouse_arriba=COLOR_AZUL_OSCURO)
        
        # Colocamos la imagen que corresponda segun si hay o no sonido 
        if sonido_activo:
            pantalla.blit(img_sonido, rect_sonido.topleft)
        else:
            pantalla.blit(img_sonido_mute, rect_sonido_mute.topleft)

        pantalla.blit(TITULO_MENU, MENU_RECT)

        # Recorremos los botones y cambiamos de color segun corresponda, despues los vuelve a dibujar en la superficie
        for boton in [BOTON_JUGAR, BOTON_SALIR]:
            boton.cambiar_color(pos_mouse)
            boton.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_JUGAR.chequear_input(pos_mouse):
                    jugar()
                if BOTON_SALIR.chequear_input(pos_mouse):
                    pygame.quit()
                    sys.exit()
                if rect_sonido.collidepoint(pos_mouse) or rect_sonido_mute.collidepoint(pos_mouse):
                    if sonido_activo == True:
                        pygame.mixer.music.set_volume(0)
                        sonido_activo = False
                    else:
                        pygame.mixer.music.set_volume(0.2)
                        sonido_activo = True
        
        pygame.display.update()


menu_principal()


