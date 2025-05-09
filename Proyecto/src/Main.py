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
    {'name': 'Aatrox', 'details': 'Details about Aatrox', 'image': 'Aatrox_icon'},
    {'name': 'Ahri'},
    {'name': 'Akali'},
    {'name': 'Akshan'},
    {'name': 'Alistar'},
    {'name': 'Ambessa'},
    {'name': 'Amumu'},
    {'name': 'Anivia'},
    {'name': 'Caitlyn'},
    {'name': 'Jhin'},
    {'name': 'Karthus'},
    {'name': 'Maokai'},
    {'name': 'Nautilus'},
    {'name': 'TahmKench'},
    {'name': 'Twitch'}
]
items_list = [
    {'name': 'Bloodthirster'},
    {'name': 'Guinsoo'},
    {'name': 'Opportunity'},
    {'name': 'Jaksho'},
    {'name': 'Thornmail'},
    {'name': 'SpiritVisage'},
    {'name': 'BlackfireTorch'}
]

# Imagenes de los campeones e items
Aatrox_icon = pygame.image.load('Proyecto/src/Assets/Images/Iconos/Aatrox_icon.png')












#Creo la pantalla
pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))
pygame.display.set_caption("TFT de la salada")

font = pygame.font.Font(None, 36)

menu_options = ['Inicio', 'Campeones', 'Guia', 'Salir']
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

def champion_details(champion):
    # Aquí crearías una ventana para mostrar los detalles del campeón
    print(f"Detalles de {champion['name']}: {champion['details']}")
    # Puedes implementar una nueva ventana si deseas mostrar los detalles en pantalla

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

