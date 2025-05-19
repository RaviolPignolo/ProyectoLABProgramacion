import importlib
import os
import pygame


items_list = [
    {'name': 'Bloodthirster', 'image': 'Proyecto/src/Assets/Images/Items/Bloodthirster_item.png'},
    {'name': 'GuinsoosRageblade', 'image': 'Proyecto/src/Assets/Images/Items/GuinsoosRageblade_item.png'},
    {'name': 'Opportunity', 'image': 'Proyecto/src/Assets/Images/Items/Opportunity_item.png'},
    {'name': 'JakShosTheProtean', 'image': 'Proyecto/src/Assets/Images/Items/JakShoTheProtean_item.png'},
    {'name': 'Thornmail', 'image': 'Proyecto/src/Assets/Images/Items/Thornmail_item.png'},
    {'name': 'SpiritVisage', 'image': 'Proyecto/src/Assets/Images/Items/SpiritVisage_item.png'},
    {'name': 'BlackfireTorch', 'image': 'Proyecto/src/Assets/Images/Items/BlackfireTorch_item.png'},
]

x: int
y: int
image: pygame.Surface
rect: pygame.Rect

class GraficoItem:
    
    def __init__(self, x, y, item):
        self.x = x
        self.y = y
        self.image = pygame.image.load(item['name'])
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        
    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)