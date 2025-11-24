import pygame

# Pantalla
ANCHO = 900
ALTO = 650

# Paletas y Pelota
VEL_PALETAS = 5
VEL_PELOTA = 3

# Colores
COLOR_BLANCO = (255, 255, 255) # Blanco
COLOR_AMARILLO = (255, 255, 0) # Amarillo
COLOR_NEGRO = (0, 0, 0)
COLOR_AZUL_OSCURO = (2, 1, 17)

# Fonts
font_juego = "fonts\juego_font.ttf"

# Imagenes
img_fondo = pygame.image.load("assets\images\menu_sin_titulo.png")
img_sonido = pygame.image.load("assets\images\sonido_activo.png")
img_sonido_mute = pygame.image.load("assets\images\sonido_mute.png")

# Musica fondo

# Paleta
COLOR_PALETA = (0, 255, 0)
ANCHO_PALETA = 30
ALTO_PALETA = 100

# Pelota
COLOR_PELOTA = (255, 0, 0)
ANCHO_PELOTA = 20
ALTO_PELOTA = 20
