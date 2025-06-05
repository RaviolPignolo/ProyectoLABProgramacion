import importlib
import os
import pygame

# Lista de los campeones e items
champions_list = [ # Ubicación correspondiente de los iconos de los campeones
    {'name': 'Aatrox', 'image': 'Proyecto/src/Assets/Images/Iconos/Aatrox_icon.png'},
    {'name': 'Ahri',  'image': 'Proyecto/src/Assets/Images/Iconos/Ahri_icon.png'},
    {'name': 'Akali', 'image': 'Proyecto/src/Assets/Images/Iconos/Akali_icon.png'},
    {'name': 'Akshan', 'image': 'Proyecto/src/Assets/Images/Iconos/Akshan_icon.png'},
    {'name': 'Alistar', 'image': 'Proyecto/src/Assets/Images/Iconos/Alistar_icon.png'},
    {'name': 'Ambessa', 'image': 'Proyecto/src/Assets/Images/Iconos/Ambessa_icon.png'},
    {'name': 'Amumu', 'image': 'Proyecto/src/Assets/Images/Iconos/Amumu_icon.png'},
    {'name': 'Anivia', 'image': 'Proyecto/src/Assets/Images/Iconos/Anivia_icon.png'},
    {'name': 'Caitlyn', 'image': 'Proyecto/src/Assets/Images/Iconos/Caitlyn_icon.png'},
    {'name': 'Jhin', 'image': 'Proyecto/src/Assets/Images/Iconos/Jhin_icon.png'},
    {'name': 'Karthus', 'image': 'Proyecto/src/Assets/Images/Iconos/Karthus_icon.png'},
    {'name': 'Maokai', 'image': 'Proyecto/src/Assets/Images/Iconos/Maokai_icon.png'},
    {'name': 'Nautilus', 'image': 'Proyecto/src/Assets/Images/Iconos/Nautilus_icon.png'},
    {'name': 'TahmKench', 'image': 'Proyecto/src/Assets/Images/Iconos/TahmKench_icon.png'},
    {'name': 'Twitch', 'image': 'Proyecto/src/Assets/Images/Iconos/Twitch_icon.png'},
]

PANTALLA_ANCHO = 1280
PANTALLA_ALTO = 720
CELDA_ANCHO = 80
CELDA_ALTO =  80
MAX_CELDAS_X = PANTALLA_ANCHO // CELDA_ANCHO
MAX_CELDAS_Y = int(PANTALLA_ALTO / 1.5) // CELDA_ALTO

y: int
x: int
image: pygame.Surface
rect: pygame.Rect

class GraficoPersonaje:

    def __init__(self, x, y, campeon):
        "Constructor"
        self.x = x
        self.y = y
        self.image = pygame.image.load(campeon['image'])
        self.image = pygame.transform.scale(self.image, (CELDA_ANCHO, CELDA_ALTO))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        
        
    def movimiento(self, direccion, cantidad):
        "Mueve el personaje en la dirección indicada por las casillas"
        if(direccion == "up"):
            self.y -= cantidad * CELDA_ALTO
        if(direccion == "down"):
            self.y += cantidad * CELDA_ALTO
        if(direccion == "left"):
            self.x -= cantidad * CELDA_ANCHO
        if(direccion == "right"):
            self.x += cantidad * CELDA_ANCHO
            
        self.rect.topleft = (self.x, self.y)
            
    def dibujar(self, pantalla):
        "Dibuja el icono del campeon"
        pantalla.blit(self.image, self.rect)
        
    def colision(self, another_champion, proximo_x, proximo_y):
        "Verifica que los campeones no se superpongan"
        temp_rect = self.rect.copy()
        temp_rect.topleft = (proximo_x, proximo_y)
        return temp_rect.colliderect(another_champion.rect)