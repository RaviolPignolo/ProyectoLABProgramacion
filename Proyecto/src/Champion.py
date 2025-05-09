import importlib
import os
import math
import pygame
from dataclasses import field
from .Item import Item

CHAMPIONS_FOLDER = "Proyecto.src.Champions" # Carpeta que contiene a los campeones


# Éstos dos métodos son para que el Main pueda cargar los campeones correctamente desde sus archivos .py

"""Método para cargas los campeones"""
def load_champion(champion_name: str):
    module_name = f"{CHAMPIONS_FOLDER}.{champion_name}"
    try:
        module = importlib.import_module(module_name)
        champ_class = getattr(module, champion_name)
        return champ_class()
    except (ModuleNotFoundError, AttributeError):
        raise ImportError(f"No se encontró el campeón {champion_name} en {module_name}")

"""Método para listar los campeones"""
def list_champions():
    champions = []
    for filename in os.listdir(CHAMPIONS_FOLDER):
        if filename.endswith(".py") and filename != "__init__.py":
            champions.append(filename[:-3])
    return champions


# https://wiki.leagueoflegends.com/en-us/Champion_statistic
class Champion:
    name: str
    title: str
    level: int
    its_alive: bool = True
    
    q_level: int
    w_level: int
    e_level: int
    r_level: int

    """Valores base del campeón"""
    base_hp: float
    base_hp_g: float
    base_hp_regen: float
    base_hp_regen_g: float
    base_mana: float
    base_mana_g: float
    base_mana_regen: float
    base_mana_regen_g: float
    base_energy: float
    base_energy_regen: float
    base_ad: float
    base_ad_g: float
    base_armor: float
    base_armor_g: float
    base_mr: float
    base_mr_g: float
    base_range: float
    base_move_speed: float
    baseAS: float
    
    """Valores actuales que se actualizan con subidas de nivel o adquiriendo objetos"""
    actual_ap: float
    actual_healshield_power: float
    actual_tenacity: float
    actual_slow_resist: float
    actual_crit_chance: float
    actual_crit_damage: float
    actual_bonus_armor: float # armadura obtenida de fuentes que no sean subir de nivel
    actual_total_armor: float # actual_armor + actual_bonus_armor
    actual_armorpen_flat: float
    actual_armorpen_percent: float
    actual_bonus_mr: float # mr obtenido de fuentes que no sean subir de nivel
    actual_total_mr: float # actual_mr + actual_bonus_mr
    actual_magicpen_flat: float
    actual_magicpen_percent: float
    actual_lifesteal: float
    actual_physicvamp: float
    actual_omnivamp: float
    actual_ah: float
    as_ratio: float
    bonus_as: float
    actual_as: float
    actual_as_ratio: float
    actual_bonus_as_level: float
    actual_bonus_as_external: float
    """Se calculan despues del constructor con 'def __post_init__()'"""
    actual_hp: float = field(init=False)
    actual_hp_regen: float = field(init=False)
    actual_mana: float = field(init=False)
    actual_mana_regen: float = field(init=False)
    actual_ad: float = field(init=False)
    actual_armor: float = field(init=False)
    actual_mr: float = field(init=False)
    actual_range: float = field(init=False)
    actual_move_speed: float = field(init=False)
    

    """Constructor"""
    def __init__(self, name, title, level, base_hp, base_hp_g, base_hp_regen, base_hp_regen_g, base_mana, base_mana_g, base_mana_regen, base_mana_regen_g, base_energy, base_energy_g, base_ad, base_ad_g, base_armor, base_armor_g, base_mr, base_mr_g, base_range, base_move_speed, base_as, as_ratio, bonus_as):
        self.name = name
        self.title = title
        self.level = level
        self.base_hp = base_hp
        self.base_hp_g = base_hp_g
        self.base_hp_regen = base_hp_regen
        self.base_hp_regen_g = base_hp_regen_g
        self.base_mana = base_mana
        self.base_mana_g = base_mana_g
        self.base_mana_regen = base_mana_regen
        self.base_mana_regen_g = base_mana_regen_g
        self.base_energy = base_energy
        self.base_energy_regen = base_energy_g
        self.base_ad = base_ad
        self.base_ad_g = base_ad_g
        self.base_armor = base_armor
        self.base_armor_g = base_armor_g
        self.base_mr = base_mr
        self.base_mr_g = base_mr_g
        self.base_range = base_range
        self.base_move_speed = base_move_speed
        self.baseAS = base_as
        self.as_ratio = as_ratio
        self.bonus_as = bonus_as
        self.__post_init__() # Post constructor

    """Post Constructor"""
    def __post_init__(self):
        self.actual_hp = self.base_hp
        self.actual_hp_regen = self.base_hp_regen
        self.actual_mana = self.base_mana
        self.actual_mana_regen = self.base_mana_regen
        self.actual_ad = self.base_ad
        self.actual_armor = self.base_armor
        self.actual_mr = self.base_mr
        self.actual_range = self.base_range
        self.actual_move_speed = self.base_move_speed
        self.actual_healshield_power = 0
        self.actual_tenacity = 0
        self.actual_slow_resist = 0
        self.actual_ap = 0
        self.actual_crit_chance = 0
        self.actual_crit_damage = 0
        self.actual_bonus_armor = 0 
        self.actual_total_armor = self.actual_armor + self.actual_bonus_armor
        self.actual_armorpen_flat = 0
        self.actual_armorpen_percent = 0
        self.actual_bonus_mr = 0
        self.actual_total_mr = self.actual_mr + self.actual_bonus_mr
        self.actual_magicpen_flat = 0
        self.actual_magicpen_percent = 0
        self.actual_lifesteal = 0
        self.actual_physicvamp = 0
        self.actual_omnivamp = 0
        self.actual_ah = 0
        self.actual_as = self.baseAS
        self.actual_as_ratio = self.as_ratio
        self.actual_bonus_as_level = 0.00000
        self.actual_bonus_as_external = 0.00000
        self.total_bonus_as = 0
        self.items = [None] * 6 # Iniciación del inventario
        self.effects = [None] * 10 # Iniciación del espacio para efectos



    """Método para subir de nivel"""
    def level_up(self):
        if self.level < 18:
            print("////////// LEVEL UP! \\\\\\\\\\")
            self.level += 1
            self.actual_hp = (self.base_hp + self.base_hp_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_hp_regen = (self.base_hp_regen + self.base_hp_regen_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_mana = (self.base_mana + self.base_mana_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_mana_regen = (self.base_mana_regen + self.base_mana_regen_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_ad = (self.base_ad + self.base_ad_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_armor = (self.base_armor + self.base_armor_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_total_armor = self.actual_armor + self.actual_bonus_armor
            self.actual_mr = (self.base_mr + self.base_mr_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_total_mr = self.actual_mr + self.actual_bonus_mr
            """Actualización del crecimiento de la velocidad de ataque por nivel"""
            self.actual_bonus_as_level += self.as_ratio * self.bonus_as * (0.7025 + 0.0175 * (self.level - 1))
            """Cálculo de la velocidad de ataque con acumulación aditiva"""
            self.total_bonus_as = self.actual_bonus_as_level + self.actual_bonus_as_external
            self.actual_as = self.baseAS * (1 + self.total_bonus_as)
        else:
            print("Ya has alcanzado el nivel máximo")
            
            
    """Método para subir de nivel las habilidades"""
    def level_up_hability(self, hability):
        if(hability == "Q"):
            if(self.q_level == 5):
                print("No se puede subir de nivel la habilidad")
            else:
                self.q_level = self.q_level + 1
                print(f"La habilidad Q de {self.name} subió a nivel {self.q_level}")
                
        if(hability == "W"):
            if(self.w_level == 5):
                print("No se puede subir de nivel la habilidad")
            else:
                self.w_level = self.w_level + 1
                print(f"La habilidad W de {self.name} subió a nivel {self.e_level}")
                
        if(hability == "E"):
            if(self.e_level == 5):
                print("No se puede subir de nivel la habilidad")
            else:
                self.e_level = self.e_level + 1
                print(f"La habilidad E de {self.name} subió a nivel {self.w_level}")
                
        if(hability == "R"):
            if(self.r_level == 3):
                print("No se puede subir de nivel la habilidad")
            else:
                self.r_level = self.r_level + 1
                print(f"La habilidad R de {self.name} subió a nivel {self.r_level}")


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= MÉTODOS RELACIONADOS CON EL SEGUIMIENTO DE LAS ESTADISTICAS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    """Método para obtener información básica"""
    def simple_stats(self):
        print("Campeón: ", self.name)
        print("Nivel: ", self.level)
        print("Salud: ", self.actual_hp)
        print("Regeneración de Salud: ", self.actual_hp_regen)
        print("Mana: ", self.actual_mana)
        print("Regeneración de Mana: ", self.actual_mana_regen)
        print("AD: ", self.actual_ad)
        print("AS: ", self.actual_as, "%")
        print("AP: ", self.actual_ap)
        print("Armadura: ", self.actual_total_armor)
        print("Resistencia Mágica: ", self.actual_total_mr)
        #velocidad de ataque tehe
        print("Ability Haste: ", self.actual_ah)
        print("Chance de Critico: ", self.actual_crit_chance,"%")
        print("Velocidad de movimiento: ", self.actual_move_speed)

    """Método para obtener información extra"""
    def extended_stats(self):
        print("Poder de Curaciones y Escudos: ", self.actual_healshield_power,"%")
        print("Letalidad: ", self.actual_armorpen_flat)
        print("Penetración de Armadura porcentual: ", self.actual_armorpen_percent,"%")
        print("Penetración de Resistencia Mágica plana: ", self.actual_magicpen_flat)
        print("Penetración de Resistencia Mágica porcentual: ", self.actual_magicpen_percent,"%")
        print("Robo de Vida: ", self.actual_lifesteal,"%")
        print("Vampirismo: ", self.actual_omnivamp,"%")
        print("Rango de ataque: ", self.actual_range)
        print("Tenacidad: ", self.actual_tenacity,"%")

    """Método para obtener informacion detallada de la velocidad de ataque"""
    def as_peed(self):
        print(f"Actual Attack Speed: {self.actual_as:.3f}")
        print(f"Base Attack Speed: {self.baseAS}")
        print(f"Actual Bonus Attack Speed External: {self.actual_bonus_as_external:.3}")
        print(f"Actual Bonus Attack Speed Leveled: {self.actual_bonus_as_level:.3}")
        print(f"Total Bonus Attack Speed: {math.ceil(self.total_bonus_as * 1000) / 10:.3f}%")
        print(f"Level: {self.level}")
        print(f"Actual Attack Speed Ratio: {self.actual_as_ratio}")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= MÉTODOS RELACIONADOS CON LOS ITEMS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    """Método para agregar un item al inventario"""
    def add_item(self, item):
        for i in range(len(self.items)):
            if self.items[i] is None:
                self.items[i] = item
                self.update_stats(item, add=True)
                print(f"[{self.name}] Item: {item.name} añadido al espacio {i + 1}.")
                return
        print("El inventario está lleno.")

    
    """Método para eliminar un item del inventario"""
    def remove_item(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items[i] = None
                self.update_stats(item, add=False)
                print(f"[{self.name}] Item: {item.name} eliminado del espacio {i + 1}.")
                return
        print("No se encontró el item.")

    
    """Método para listar los items del inventario"""
    def list_items(self):
        item_list = []
        for i, item in enumerate(self.items):
            if item is not None:
                item_list.append(item.name)
        return item_list

    """Método para actualizar las estadísticas del campeón despues de agregar o eliminar un item"""
    def update_stats(self, item, add=True):
        factor = 1 if add else -1
        self.actual_hp += item.hp * factor
        self.actual_hp_regen += item.hp_regen * factor
        self.actual_mana += item.mana * factor
        self.actual_mana_regen += item.mana_regen * factor
        self.actual_ad += item.ad * factor
        self.actual_ap += item.ap * factor
        self.actual_bonus_armor += item.armor * factor
        self.actual_total_armor = self.actual_armor + self.actual_bonus_armor
        self.actual_bonus_mr += item.mr * factor
        self.actual_total_mr = self.actual_mr + self.actual_bonus_mr
        self.actual_healshield_power += item.healshield_power * factor
        self.actual_tenacity += item.tenacity * factor
        self.actual_crit_chance += item.crit_chance * factor
        self.actual_crit_damage += item.crit_damage * factor
        self.actual_armorpen_flat += item.armorpen_flat * factor
        self.actual_armorpen_percent += item.armorpen_percent * factor
        self.actual_magicpen_flat += item.magicpen_flat * factor
        self.actual_magicpen_percent += item.magicpen_percent * factor
        self.actual_lifesteal += item.lifesteal * factor
        self.actual_ah += item.ah * factor
        self.actual_move_speed += item.movespeed_flat * factor
        self.actual_move_speed += item.movespeed_percent * factor
        self.actual_bonus_as_external += item.as_ * factor
        self.total_bonus_as = self.actual_bonus_as_level + self.actual_bonus_as_external
        self.actual_as = self.baseAS * (1 + self.total_bonus_as)


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= MÉTODOS RELACIONADOS CON LOS EFECTOS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    """Método para agregar un efecto"""
    def add_item(self, item):
        for i in range(len(self.items)):
            if self.items[i] is None:
                self.items[i] = item
                self.update_stats(item, add=True)
                print(f"[{self.name}] Item: {item.name} añadido al espacio {i + 1}.")
                return
        print("El inventario está lleno.")

    
    """Método para eliminar un efecto"""
    def remove_item(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items[i] = None
                self.update_stats(item, add=False)
                print(f"[{self.name}] Item: {item.name} eliminado del espacio {i + 1}.")
                return
        print("No se encontró el item.")

    
    """Método para listar los efectos"""
    def list_items(self):
        item_list = []
        for i, item in enumerate(self.items):
            if item is not None:
                item_list.append(item.name)
        return item_list











# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= MÉTODOS RELACIONADOS CON EL COMBATE =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    """ Método para el sistema de ataque"""
    def sistema_pelea(self, Champion):
        turno: int
        tiempo: int
        
        while(self.its_alive and Champion.its_alive == True):
            print("--------------------------------------")
            print(f"----| {self.name} |------------------")
            print(f"----| HP: {self.actual_hp} |-----------")
            print(f"----| MP: {self.actual_mana} |---------")
            print("--------------------------------------")
            print(f"----| {Champion.name} |------------------")
            print(f"----| HP: {Champion.actual_hp} |-----------")
            print(f"----| MP: {Champion.actual_mana} |---------")
            print("--------------------------------------")
            print("----| Turno de: xxxxxx |--------------")
            print("----| Habilidades: |---------------")
            print("----| 1) Q  |---| 1) W  |---| 1) E  |---| 1) R  |")
            print("----| Comandos: |-----------------------")
            print("----| '/help' |---| '/items' |---| '/efectos' |----")
            print("----| '/detalles_habilidades' |---| '/detalles_campeon|----")
            print("-------------------------------------------------")
            """
            Acá el programa tiene que escuchar lo que escribe el usuario:
            si es 1 ejecuta la Q del campeón que tiene el turno
            si es 2 ejecuta la W del campeón que tiene el turno
            si es 3 ejecuta la E del campeón que tiene el turno
            si es 4 ejecuta la R del campeón que tiene el turno
            si es /help describe que hacen los comandos
            si es /items se muestran los items que tienen ambos campeónes, mas adelante se muestra cómo deberia verse
            si es /efectos se muestran los efectos que sufren los campeónes, mas adelante se muestra cómo deberia verse
            si es /detalles_habilidades se describen las haibilidades de los campeónes y el resultado actualizado de los cálculos que tengan
            si es /detalles_campeon se muestran las estadisticas de los campeones usando los metodos simple_stats() y extended_stats()
            """
            #pantalla que se muestra al usar /items
            print("--------------------------")
            print(f"----| {self.list_items} |----")
            print(f"----| {Champion.list_items} |----")
            print("--------------------------")
            
            #pantalla que se muestra al usar /efectos
            print("--------------------------")
            print(f"----| {self.name} |-----")
            print(f"--")
            
            
            print(f"----| {Champion.name} |----")
            
            
            #pantalla que se muestra al usar /detalles_habilidades
            
            
            #pantalla que se muestra al usar /detalles_campeon




    """--Método para inflingir daño--"""
    """Método donde 2 campeones se pelearán a muerte a base de Auto Ataques"""
    def realizar_daño(self, enemy):
        print("------------------------------------------------------------------------------------------------------")
        print(f"{self.name} ataca a {enemy.name}")
        print("------------------------------------------------------------------------------------------------------")
        print(f"{self.name}")
        print(self.simple_stats())
        print("------------------------------------------------------------------------------------------------------")
        print(f"{enemy.name}")
        print(enemy.simple_stats())
        print("------------------------------------------------------------------------------------------------------")
        
        while(self.its_alive and enemy.its_alive == True): # Mientras uno de los dos siga vivo se van a seguir peleando
            enemy.aa(self)
            self.aa(enemy)

            if(enemy.its_alive != True and self.its_alive != True): #Ambos mueren
                print(f"{self.name} y {enemy.name} murieron")
                break
            elif(enemy.its_alive != True and self.its_alive == True): #Gana self
                print(f"{enemy.name} fue derrotado por {self.name}")
                break
            elif(enemy.its_alive == True and self.its_alive != True): #Gana enemy
                print(f"{self.name} fue derrotado por {enemy.name}") 
                break
    
    # https://www.youtube.com/watch?v=zrFb18aIjyg -> Video expliacndo la armadura y resistencia mágica
    
    """Método para calcular el daño de los AA"""
    def aa(self, enemy): #self recibe daño de enemy
        #daño_total = 0
        
        if(self.actual_total_armor > 0):
            daño_total = (enemy.actual_ad / (1 + self.actual_total_armor / 100))
        else:
            daño_total = (enemy.actual_ad * (2 - (100 / (100 - self.actual_total_armor))))     
        
        daño_total = max(daño_total, 0) # Evita que el valor del daño sea negativo
        self.actual_hp -= daño_total
        self.actual_hp = max(self.actual_hp, 0) #Evita que el valor de la vida sea negativo
        
        print(f"{self.name} recibió {daño_total: .2f} de daño.")
        print(f"Salud de {self.name} actualizado a: {self.actual_hp: .2f}")


        # Cambiar de lugat el if() para que sea parte del método realizar_daño() y poder usar el método aa() como parte del kit de habilidades de los campeones
        if(self.actual_hp <= 0): # Despues de cada golpe revisa si alguno de los dos murio, si ocurre se termina el while() y se da un resultado
            self.its_alive = False        
    
            
    """Método para calcular daño dependiento el tipo"""
    def hacer_daño(self, cantidad, tipo, Champion):
        daño_total = 0
        
        if(tipo == "TRUE"):
            daño_total = cantidad
        elif(tipo == "AP"):
            if(Champion.actual_total_mr > 0):
                daño_total = (cantidad / (1 + Champion.actual_total_mr / 100))
            else:
                daño_total = (cantidad * (2 - (100 / (100 - Champion.actual_total_mr))))
        elif(tipo == "AD"):
            if(Champion.actual_total_armor > 0):
                daño_total = (cantidad / (1 + Champion.actual_total_armor / 100))
            else:
                daño_total = (cantidad * (2 - (100 / (100 - Champion.actual_total_armor))))
        else:
            print("No se reconoce el tipo de daño recibido")
        
        daño_total = max(daño_total, 0)
        Champion.actual_hp -= daño_total
        Champion.actual_hp = max(Champion.actual_hp, 0)
        
        print(f"{Champion.name} recibió {daño_total: .2f} de daño {tipo}.")
        print(f"Salud de {Champion.name} actualizado a: {Champion.actual_hp: .2f}.")            
            
    
    def pasiva(self):
        print(f"La pasiva de {self.name} hace efecto")        
            
    def q(self):
        print(f"{self.name} usa Q")
        
    def w(self):
        print(f"{self.name} usa W")
        
    def e(self):
        print(f"{self.name} usa E")
        
    def r(self):
        print(f"{self.name} usa R")    
    