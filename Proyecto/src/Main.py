from .Champion import Champion
from .Item import Item
from .Champion import load_champion
from .Item import load_item
from Proyecto.src.vista.grafico_personaje import GraficoPersonaje
from Proyecto.src.vista.grafico_personaje import champions_list
from Proyecto.src.vista.grafico_item import GraficoItem
from Proyecto.src.vista.grafico_item import items_list
import pygame
import sys

pygame.init()

PANTALLA_ANCHO = 1280
PANTALLA_ALTO = 720

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (128, 128, 128)

FONT = pygame.font.Font("Proyecto/src/Assets/Fonts/BeaufortforLOL-Medium.ttf", 36)

#Creo la pantalla
pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))
pygame.display.set_caption("TFT de la salada")


menu_options = ['Inicio', 'Campeones', 'Items', 'Guia', 'Salir']
selected_option = 0

def menu():
    "Menú del juego"
    pantalla.fill(NEGRO)
    for i, option in enumerate(menu_options):
        if i == selected_option:
            text = FONT.render(option, True, BLANCO)
        else:
            text = FONT.render(option, True, GRIS)
        text_rect = text.get_rect(center=(PANTALLA_ANCHO // 2, PANTALLA_ALTO // 2 + i * 40))
        pantalla.blit(text, text_rect)

def champion_list_menu():
    "Lista de los campeones disponibles para ver sus estadisticas base y habilidades"
    selected_champion = 0
    back_button_rect = pygame.Rect(10, 10, 100, 40)  # Define un rectángulo para el botón de "Atrás"
    champions_per_row = 5
    x_offset = 150
    y_offset = 200
    spacing_x = 140  # Espacio horizontal entre filas
    spacing_y = 120  # Espacio vertical entre filas

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if (selected_champion + champions_per_row) < len(champions_list):
                        selected_champion += champions_per_row
                elif event.key == pygame.K_UP:
                    if (selected_champion - champions_per_row) >= 0:
                        selected_champion -= champions_per_row
                elif event.key == pygame.K_RIGHT:
                    if (selected_champion % champions_per_row) < (champions_per_row - 1) and (selected_champion + 1) < len(champions_list):
                        selected_champion += 1
                elif event.key == pygame.K_LEFT:
                    if (selected_champion % champions_per_row) > 0:
                        selected_champion -= 1
                elif event.key == pygame.K_RETURN:
                    champion_details(champions_list[selected_champion])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return

        pantalla.fill(NEGRO)
        
        # Dibuja el botón de "Atrás"
        pygame.draw.rect(pantalla, BLANCO, back_button_rect)
        back_text = FONT.render('Atrás', True, NEGRO)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        pantalla.blit(back_text, back_text_rect)
        
        for i, Champion in enumerate(champions_list):
            # Calcula la posición en la cuadrícula
            row = i // champions_per_row
            col = i % champions_per_row
            x_position = x_offset + col * spacing_x
            y_position = y_offset + row * spacing_y
            
            # Cargar y dibujar la imagen del campeón
            image = pygame.image.load(Champion['image'])
            image_rect = image.get_rect(center=(x_position, y_position))
            pantalla.blit(image, image_rect)
            
            # Dibujar el nombre del campeón
            if i == selected_champion:
                text = FONT.render(Champion['name'], True, BLANCO)
            else:
                text = FONT.render(Champion['name'], True, GRIS)
            text_rect = text.get_rect(midtop=(x_position, y_position + 40))
            pantalla.blit(text, text_rect)
        
        pygame.display.update()


def items_list_menu():
    "Lista de los items disponibles para ver sus estadisticas"
    selected_item = 0
    back_button_rect = pygame.Rect(10, 10, 100, 40) # Define un rectángulo para el botón de "Atrás"
    item_per_row = 5
    x_offset = 150
    y_offset = 200
    spacing_x = 140  # Espacio horizontal entre items
    spacing_y = 120  # Espacio vertical entre filas
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if (selected_item + item_per_row) < len(items_list):
                        selected_item += item_per_row
                elif event.key == pygame.K_UP:
                    if (selected_item - item_per_row) >= 0:
                        selected_item -= item_per_row
                elif event.key == pygame.K_RIGHT:
                    if (selected_item % item_per_row) < (item_per_row - 1) and (selected_item + 1) < len(items_list):
                        selected_item += 1
                elif event.key == pygame.K_LEFT:
                    if (selected_item % item_per_row) > 0:
                        selected_item -= 1
                elif event.key == pygame.K_RETURN:
                    items_details(items_list[selected_item])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return

        pantalla.fill(NEGRO)
        
        pygame.draw.rect(pantalla, BLANCO, back_button_rect)
        back_text = FONT.render('Atrás', True, NEGRO)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        pantalla.blit(back_text, back_text_rect)
        
        for i, Item in enumerate(items_list):
            # Calcula la posición en la cuadrícula
            row = i // item_per_row
            col = i % item_per_row
            x_position = x_offset + col * spacing_x
            y_position = y_offset + row * spacing_y
            
            # Cargar y dibujar la imagen del item
            image = pygame.image.load(Item['image'])
            image_rect = image.get_rect(center=(x_position, y_position))
            pantalla.blit(image, image_rect)
            
            # Dibujar el nombre del item
            if i == selected_item:
                text = FONT.render(Item['name'], True, BLANCO)
            else:
                text = FONT.render(Item['name'], True, GRIS)
            text_rect = text.get_rect(midtop=(x_position, y_position + 40))
            pantalla.blit(text, text_rect)
        
        pygame.display.update()


def champion_details(champion):
    "Estadisticas y habilidades del campeón seleccionado"
    back_button_rect = pygame.Rect(10, 10, 100, 40)
    campeon_instancia = load_champion(champion['name'])
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
        back_text = FONT.render('Atrás', True, NEGRO)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        pantalla.blit(back_text, back_text_rect)
        
        image = pygame.image.load(champion['image'])
        image_rect = image.get_rect(center=(100, 200))
        pantalla.blit(image, image_rect)
        
        """
        champion_info_text = campeon_instancia.base_stats()
        y_offset = 300
        for line in champion_info_text.split('\n'):
            champion_info_render = FONT.render(line, True, BLANCO)
            pantalla.blit(champion_info_render, (100, y_offset))
            y_offset += 50
        """
        
        champion_info_list = campeon_instancia.base_stats()
        y_offset = 300
        for stat in champion_info_list:
            if stat["icon"]:
                icon_img = pygame.image.load(stat["icon"])
                icon_img  = pygame.transform.scale(icon_img, (25, 25))
                pantalla.blit(icon_img, (100, y_offset))
                text_x = 140
            else:
                text_x = 100
                
            value_text = FONT.render(str(stat["value"]), True, BLANCO)
            pantalla.blit(value_text, (text_x, y_offset))
            y_offset += 40
        
        pygame.display.update()

def items_details(item):
    "Estadisticas del item seleccionado"
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
        back_text = FONT.render('Atrás', True, NEGRO)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        pantalla.blit(back_text, back_text_rect)
        
        image = pygame.image.load(item['image'])
        image_rect = image.get_rect(center=(100, 200))
        pantalla.blit(image, image_rect)
        
        item_info_list = item_instancia.item_info()
        y_offset = 300
        for stat in item_info_list:
            if stat["icon"]:
                icon_img = pygame.image.load(stat["icon"])
                icon_img = pygame.transform.scale(icon_img, (25, 25))
                pantalla.blit(icon_img, (100, y_offset))
                text_x = 140
            else:
                text_x = 100
            
            value_text = FONT.render(str(stat["value"]), True, BLANCO)
            pantalla.blit(value_text, (text_x, y_offset))
            y_offset += 40
        
        pygame.display.update()

def pantalla_select():
    "Pantalla para la selección del campeón que usará cada jugador"
    """
    La idea es que al darle a Inicio te lleve a ésta ventana, donde los 2 jugadores seleccionarán la composición de su equipo con los campeones.
    Los campeones se almacenen en las lista para el equipo rojo y azul y luego te lleva a la pantalla de juego, donde los campones estarán ya ubicados
    y en base a algun resultado de orden, debajo del mapa se verá de quién es el turno actual, con un marco rojo o azul para identificar a que equipo pertenece
    y algun efecto para que sobresalte si es el que ocupa el turno actual.
    Debajo de cada uno se verá la vida y maná/energia/furia que tiene.
    
    Más abajo y ocupando más espacio, se verá en detalle el icono, vida, maná/energia/furia, habilidades(con sus puntos), item y efectos.
    Acompañado de opciones para usar alguna habilidad, movimiento, ataque básico, uso de item, o información sobre el campeón, sus habilidades e items.
    """
    
    lista_rojo = []
    lista_azul = []
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        
        
        pygame.display.update()

def pantalla_juego():
    "Pantalla del juego"
    CELDA_ANCHO = 80
    CELDA_ALTO = 80
    MAX_CELDAS_X = PANTALLA_ANCHO // CELDA_ANCHO
    MAX_CELDAS_Y = int(PANTALLA_ALTO / 1.5) // CELDA_ALTO

    campeon1_select: str
    campeon2_select: str
    
    # Le paso los campeones que se usarán, más adelante la idea es que reciba una lista
    campeon1_select = "Karthus" 
    campeon2_select = "Twitch"

    # Busco los campeones seleccionados en la lista
    campeon1_dict = next(c for c in champions_list if c['name'] == campeon1_select)
    campeon2_dict = next(c for c in champions_list if c['name'] == campeon2_select)
    
    #Inicio la parte lógica de los campeones
    campeon1_logic = load_champion(campeon1_select)
    campeon2_logic = load_champion(campeon2_select)
    
    # Les asigno la imagen y lógica a los campeones
    campeon1 = GraficoPersonaje(3 * CELDA_ANCHO, 2 * CELDA_ALTO, campeon1_dict)
    campeon1.champion = campeon1_logic
    
    campeon2 = GraficoPersonaje(6 * CELDA_ANCHO, 4 * CELDA_ALTO, campeon2_dict)
    campeon2.champion = campeon2_logic
    # campeon1.champion.q(campeon2.champion)

    arena_imagen = pygame.image.load('Proyecto/src/Assets/Images/Arena.png') # Cargo la imagen de la zona de pelea
    arena_imagen = pygame.transform.scale(arena_imagen, (PANTALLA_ANCHO, int(PANTALLA_ALTO / 1.5)))
    
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEMOTION):
                print("Posición:", event.pos)
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_DOWN):
                    if (campeon1.y // CELDA_ALTO < MAX_CELDAS_Y - 1) and not (campeon1.colision(campeon2, campeon1.x, (campeon1.y + 1 * CELDA_ALTO))):
                        campeon1.movimiento("down", 1)
                elif (event.key == pygame.K_UP):
                    if (campeon1.y // CELDA_ALTO > 0) and not (campeon1.colision(campeon2, campeon1.x, (campeon1.y - 1 * CELDA_ALTO))):
                        campeon1.movimiento("up", 1) 
                elif (event.key == pygame.K_RIGHT):
                    if (campeon1.x // CELDA_ANCHO < MAX_CELDAS_X -1) and not (campeon1.colision(campeon2, (campeon1.x + 1 * CELDA_ANCHO), campeon1.y)):
                        campeon1.movimiento("right", 1)
                elif (event.key == pygame.K_LEFT):
                    if (campeon1.x // CELDA_ANCHO > 0) and not (campeon1.colision(campeon2, (campeon1.x - 1 * CELDA_ANCHO), campeon1.y)):
                        campeon1.movimiento("left", 1)
                
        pantalla.fill(NEGRO)
        pantalla.blit(arena_imagen, (0, 0))
        campeon1.dibujar(pantalla)
        campeon2.dibujar(pantalla)
        
        # Dibujo la cuadrilla del juego
        for x in range(0, PANTALLA_ANCHO, CELDA_ANCHO):
            for y in range(0, int(PANTALLA_ALTO / 1.5), CELDA_ALTO):
                rect = pygame.Rect(x, y, CELDA_ANCHO, CELDA_ALTO)
                pygame.draw.rect(pantalla, BLANCO, rect, 1)
                
                text = FONT.render(f"{x // CELDA_ANCHO}, {y // CELDA_ALTO}", True, BLANCO)
                pantalla.blit(text, (x + 5, y + 5))
                
        pygame.display.update()




def main():
    "Menú principal"
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
                        pantalla_juego()
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
#Aatrox = load_champion("Aatrox")
#Ahri = load_champion("Ahri")
#Akali = load_champion("Akali")
#Akshan = load_champion("Akshan")
#Alistar = load_champion("Alistar")
#Ambessa = load_champion("Ambessa")
#Amumu = load_champion("Amumu")
#Anivia = load_champion("Anivia")
#Caitlyn = load_champion("Caitlyn")
#Jhin = load_champion("Jhin")
#Karthus = load_champion("Karthus")
#Maokai = load_champion("Maokai")
#Nautilus = load_champion("Nautilus")
#TahmKench = load_champion("TahmKench")
#Twitch = load_champion("Twitch")

# Items
#Bloodthirster = load_item("Bloodthirster")
#Guinsoo = load_item("Guinsoo")
#Opportunity = load_item("Opportunity")
#Jaksho = load_item("Jaksho")
#Thornmail = load_item("Thornmail")
#SpiritVisage = load_item("SpiritVisage")
#BlackfireTorch = load_item("BlackfireTorch")

