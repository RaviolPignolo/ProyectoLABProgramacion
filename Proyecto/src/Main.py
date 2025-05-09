from .Champion import Champion
from .Item import Item
from .Champion import load_champion
from .Item import load_item
import pygame
import sys

pygame.init()

PANTALLA_ANCHO = 800
PANTALLA_ALTO = 600

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Lista de los campeones e items
champions_list = [
    {'name': 'Aatrox', 'details': 'Details about Aatrox', 'image': 'Proyecto/src/Assets/Images/Iconos/Aatrox_icon.png'},
    {'name': 'Ahri', 'details': 'Details about Ahri', 'image': 'Proyecto/src/Assets/Images/Iconos/Ahri_icon.png'},
    {'name': 'Akali', 'details': 'Details about Akali', 'image': 'Proyecto/src/Assets/Images/Iconos/Akali_icon.png'},
    {'name': 'Akshan', 'details': 'Details about Akshan', 'image': 'Proyecto/src/Assets/Images/Iconos/Akshan_icon.png'},
    {'name': 'Alistar', 'details': 'Details about Alistar', 'image': 'Proyecto/src/Assets/Images/Iconos/Alistar_icon.png'},
    {'name': 'Ambessa', 'details': 'Details about Ambessa', 'image': 'Proyecto/src/Assets/Images/Iconos/Ambessa_icon.png'},
    {'name': 'Amumu', 'details': 'Details about Amumu', 'image': 'Proyecto/src/Assets/Images/Iconos/Amumu_icon.png'},
    {'name': 'Anivia', 'details': 'Details about Anivia', 'image': 'Proyecto/src/Assets/Images/Iconos/Anivia_icon.png'},
    {'name': 'Caitlyn', 'details': 'Details about Caitlyn', 'image': 'Proyecto/src/Assets/Images/Iconos/Caitlyn_icon.png'},
    {'name': 'Jhin', 'details': 'Details about Jhin', 'image': 'Proyecto/src/Assets/Images/Iconos/Jhin_icon.png'},
    {'name': 'Karthus', 'details': 'Details about Karthus', 'image': 'Proyecto/src/Assets/Images/Iconos/Karthus_icon.png'},
    {'name': 'Maokai', 'details': 'Details about Maokai', 'image': 'Proyecto/src/Assets/Images/Iconos/Maokai_icon.png'},
    {'name': 'Nautilus', 'details': 'Details about Nautilus', 'image': 'Proyecto/src/Assets/Images/Iconos/Nautilus_icon.png'},
    {'name': 'TahmKench', 'details': 'Details about TahmKench', 'image': 'Proyecto/src/Assets/Images/Iconos/TahmKench_icon.png'},
    {'name': 'Twitch', 'details': 'Details about Twitch', 'image': 'Proyecto/src/Assets/Images/Iconos/Twitch_icon.png'},
]
items_list = [
    {'name': 'Bloodthirster', 'details': 'Details about Bloodthirster', 'image': 'Proyecto/src/Assets/Images/Items/Bloodthirster_item.png'},
    {'name': 'Guinsoo', 'details': 'Details about Guinsoo', 'image': 'Proyecto/src/Assets/Images/Items/GuinsoosRageblade_item.png'},
    {'name': 'Opportunity', 'details': 'Details about Opportunity', 'image': 'Proyecto/src/Assets/Images/Items/Opportunity_item.png'},
    {'name': 'Jaksho', 'details': 'Details about Jaksho', 'image': 'Proyecto/src/Assets/Images/Items/JakShoTheProtean_item.png'},
    {'name': 'Thornmail', 'details': 'Details about Thornmail', 'image': 'Proyecto/src/Assets/Images/Items/Thornmail_item.png'},
    {'name': 'SpiritVisage', 'details': 'Details about SpiritVisage', 'image': 'Proyecto/src/Assets/Images/Items/SpiritVisage_item.png'},
    {'name': 'BlackfireTorch', 'details': 'Details about BlackfireTorch', 'image': 'Proyecto/src/Assets/Images/Items/BlackfireTorch_item.png'},
]




#Creo la pantalla
pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))
pygame.display.set_caption("TFT de la salada")

font = pygame.font.Font(None, 36)

menu_options = ['Inicio', 'Campeones', 'Items', 'Guia', 'Salir']
selected_option = 0

def menu():
    pantalla.fill(NEGRO)
    for i, option in enumerate(menu_options):
        if i == selected_option:
            text = font.render(option, True, (BLANCO))
        else:
            text = font.render(option, True, (100, 100, 100))
        text_rect = text.get_rect(center=(PANTALLA_ANCHO // 2, PANTALLA_ALTO // 2 + i * 40))
        pantalla.blit(text, text_rect)

def champion_list_menu():
    selected_champion = 0
    back_button_rect = pygame.Rect(10, 10, 100, 40) # Define un rectángulo para el botón de "Atrás"
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_champion = (selected_champion + 1) % len(champions_list)
                elif event.key == pygame.K_UP:
                    selected_champion = (selected_champion - 1) % len(champions_list)
                elif event.key == pygame.K_RETURN:
                    # Aquí puedes mostrar los detalles del campeón seleccionado
                    champion_details(champions_list[selected_champion])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return # Regresar al menú anterior

        pantalla.fill(NEGRO)
        
        # Dibuja el botón de "Atrás"
        pygame.draw.rect(pantalla, BLANCO, back_button_rect)
        back_text = font.render('Atrás', True, NEGRO)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        pantalla.blit(back_text, back_text_rect)
        
        for i, Champion in enumerate(champions_list):
            image = pygame.image.load(Champion['image'])
            image_rect = image.get_rect(center=(100, 200 + i * 60))
            pantalla.blit(image, image_rect)
            
            if i == selected_champion:
                text = font.render(Champion['name'], True, BLANCO)
            else:
                text = font.render(Champion['name'], True, (100, 100, 100))
            text_rect = text.get_rect(midleft=(150, 200 + i * 60))
            pantalla.blit(text, text_rect)
        
        pygame.display.update()


def items_list_menu():
    selected_item = 0
    back_button_rect = pygame.Rect(10, 10, 100, 40) # Define un rectángulo para el botón de "Atrás"
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(items_list)
                elif event.key == pygame.K_UP:
                    selected_champion = (selected_item - 1) % len(items_list)
                elif event.key == pygame.K_RETURN:
                    # Aquí puedes mostrar los detalles del campeón seleccionado
                    items_details(items_list[selected_item])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return # Regresar al menú anterior

        pantalla.fill(NEGRO)
        
        # Dibuja el botón de "Atrás"
        pygame.draw.rect(pantalla, BLANCO, back_button_rect)
        back_text = font.render('Atrás', True, NEGRO)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        pantalla.blit(back_text, back_text_rect)
        
        for i, Item in enumerate(items_list):
            image = pygame.image.load(Item['image'])
            image_rect = image.get_rect(center=(100, 200 + i * 60))
            pantalla.blit(image, image_rect)
            
            if i == selected_item:
                text = font.render(Item['name'], True, BLANCO)
            else:
                text = font.render(Item['name'], True, (100, 100, 100))
            text_rect = text.get_rect(midleft=(150, 200 + i * 60))
            pantalla.blit(text, text_rect)
        
        pygame.display.update()


def champion_details(champion):
    # Aquí crearías una ventana para mostrar los detalles del campeón
    print(f"Detalles de {champion['name']}: {champion['details']}")
    # Puedes implementar una nueva ventana si deseas mostrar los detalles en pantalla

def items_details(item):
    back_button_rect = pygame.Rect(10, 10, 100, 40)
    item_instancia = load_item(item['name'])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return

        pantalla.fill(NEGRO)
        
        pygame.draw.rect(pantalla, BLANCO, back_button_rect)
        back_text = font.render('Atrás', True, NEGRO)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        pantalla.blit(back_text, back_text_rect)
        
        image = pygame.image.load(item['image'])
        image_rect = image.get_rect(center=(100, 200))
        pantalla.blit(image, image_rect)
        
        item_info_text = item_instancia.item_info()
        item_info_render = font.render(item_info_text, True, BLANCO)
        pantalla.blit(item_info_render, (20, 80))
        
        pygame.display.update()

def main():
    global selected_option
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_option] == 'Salir':
                        pygame.quit()
                        sys.exit()
                    elif menu_options[selected_option] == 'Inicio':
                        # Aquí iría el código para iniciar el juego
                        pass
                    elif menu_options[selected_option] == 'Campeones':
                        champion_list_menu()
                        pass
                    elif menu_options[selected_option] == "Items":
                        items_list_menu()
                        pass
                    elif menu_options[selected_option] == 'Diccionario':
                        # Aquí iría el código para mostrar el diccionario
                        pass

        menu()
        pygame.display.update()

if __name__ == '__main__':
    main()







# Campeones
Aatrox = load_champion("Aatrox")
Ahri = load_champion("Ahri")
Akali = load_champion("Akali")
Akshan = load_champion("Akshan")
Alistar = load_champion("Alistar")
Ambessa = load_champion("Ambessa")
Amumu = load_champion("Amumu")
Anivia = load_champion("Anivia")
Caitlyn = load_champion("Caitlyn")
Jhin = load_champion("Jhin")
Karthus = load_champion("Karthus")
Maokai = load_champion("Maokai")
Nautilus = load_champion("Nautilus")
TahmKench = load_champion("TahmKench")
Twitch = load_champion("Twitch")

# Items
Bloodthirster = load_item("Bloodthirster")
Guinsoo = load_item("Guinsoo")
Opportunity = load_item("Opportunity")
Jaksho = load_item("Jaksho")
Thornmail = load_item("Thornmail")
SpiritVisage = load_item("SpiritVisage")
BlackfireTorch = load_item("BlackfireTorch")

