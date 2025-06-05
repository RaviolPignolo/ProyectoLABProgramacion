import importlib
import os
import math
from dataclasses import field
from .Item import Item

CHAMPIONS_FOLDER = "Proyecto.src.Champions" # Carpeta que contiene a los campeones

stat_icon = { # Ubicación de los iconos correspondientes a las estadisticas
    #"Gold": "Proyecto/src/Assets/Images/StatIcon/Gold_icon.png", -> Ésto seguramente separe la logica de inventario de la logica de Champion
    "Health": "Proyecto/src/Assets/Images/StatIcon/Health_icon.png",
    "Health Growth": "Proyecto/src/Assets/Images/StatIcon/Health_icon.png",
    "Health Regen": "Proyecto/src/Assets/Images/StatIcon/Health_regeneration_icon.png",
    "Health Regen Growth": "Proyecto/src/Assets/Images/StatIcon/Health_regeneration_icon.png",
    "Mana": "Proyecto/src/Assets/Images/StatIcon/Mana_icon.png",
    "Mana Growth": "Proyecto/src/Assets/Images/StatIcon/Mana_icon.png",
    "Mana Regen": "Proyecto/src/Assets/Images/StatIcon/Mana_regeneration_icon.png",
    "Mana Regen Growth": "Proyecto/src/Assets/Images/StatIcon/Mana_regeneration_icon.png",
    "Energy": "Proyecto/src/Assets/Images/StatIcon/Energy_icon.png",
    "Energy Regen": "Proyecto/src/Assets/Images/StatIcon/Energy_regeneration_icon.png",
    "Attack Damage": "Proyecto/src/Assets/Images/StatIcon/Attack_damage_icon.png",
    "Attack Damage Growth": "Proyecto/src/Assets/Images/StatIcon/Attack_damage_icon.png",
    "Ability Power": "Proyecto/src/Assets/Images/StatIcon/Ability_power_icon.png",
    "Attack Speed(%)": "Proyecto/src/Assets/Images/StatIcon/Attack_speed_icon.png",
    "Base Attack Speed": "Proyecto/src/Assets/Images/StatIcon/Attack_speed_icon.png",
    "Attack Speed Ratio": "Proyecto/src/Assets/Images/StatIcon/Attack_speed_icon.png",
    "Bonus Attack Speed": "Proyecto/src/Assets/Images/StatIcon/Attack_speed_icon.png",
    "Armor": "Proyecto/src/Assets/Images/StatIcon/Armor_icon.png",
    "Armor Growth": "Proyecto/src/Assets/Images/StatIcon/Armor_icon.png",
    "Magic Resistance": "Proyecto/src/Assets/Images/StatIcon/Magic_resistance_icon.png",
    "Magic Resistance Growth": "Proyecto/src/Assets/Images/StatIcon/Magic_resistance_icon.png",
    "Range": "Proyecto/src/Assets/Images/StatIcon/Range_icon.png",
    "Heal & Shield Power(%)": "Proyecto/src/Assets/Images/StatIcon/Heal_and_shield_power_icon.png",
    "Tenacity": "Proyecto/src/Assets/Images/StatIcon/Tenacity_icon.png",
    "Critical Strike Chance(%)": "Proyecto/src/Assets/Images/StatIcon/Critical_strike_chance_icon.png",
    "Critical Strike Damage(%)": "Proyecto/src/Assets/Images/StatIcon/Critical_strike_damage_icon.png",
    "Lethality": "Proyecto/src/Assets/Images/StatIcon/Armor_penetration_icon.png",
    "Armor Penetration(%)": "Proyecto/src/Assets/Images/StatIcon/Armor_penetration_icon.png",
    "MagicResist Flat Penetration": "Proyecto/src/Assets/Images/StatIcon/Magic_penetration_icon.png",
    "MagicResist Penetration(%)": "Proyecto/src/Assets/Images/StatIcon/Magic_penetration_icon.png",
    "Lifesteal(%)": "Proyecto/src/Assets/Images/StatIcon/Life_steal_icon.png",
    "Ability Haste": "Proyecto/src/Assets/Images/StatIcon/Cooldown_reduction_icon.png",
    "Movement Speed": "Proyecto/src/Assets/Images/StatIcon/Movement_speed_icon.png",
    "Movement Speed(%)": "Proyecto/src/Assets/Images/StatIcon/Movement_speed_icon.png",
}

# Éstos dos métodos son para que el Main pueda cargar los campeones correctamente desde sus archivos .py
def load_champion(champion_name: str):
    """Método para cargas los campeones"""
    module_name = f"{CHAMPIONS_FOLDER}.{champion_name}"
    try:
        module = importlib.import_module(module_name)
        champ_class = getattr(module, champion_name)
        return champ_class()
    except (ModuleNotFoundError, AttributeError):
        raise ImportError(f"No se encontró el campeón {champion_name} en {module_name}")

def list_champions():
    """Método para listar los campeones"""
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

    #Valores base del campeón
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
    
    #Valores actuales que se actualizan con subidas de nivel o adquiriendo objetos
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
    #Se calculan despues del constructor con 'def __post_init__()'
    actual_hp: float = field(init=False)
    actual_hp_regen: float = field(init=False)
    actual_mana: float = field(init=False)
    actual_mana_regen: float = field(init=False)
    actual_ad: float = field(init=False)
    actual_armor: float = field(init=False)
    actual_mr: float = field(init=False)
    actual_range: float = field(init=False)
    actual_move_speed: float = field(init=False)
    

    
    def __init__(self, name, title, level, base_hp, base_hp_g, base_hp_regen, base_hp_regen_g, base_mana, base_mana_g, base_mana_regen, base_mana_regen_g, base_energy, base_energy_g, base_ad, base_ad_g, base_armor, base_armor_g, base_mr, base_mr_g, base_range, base_move_speed, base_as, as_ratio, bonus_as):
        """Constructor"""
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

    def __post_init__(self):
        """Post Constructor"""
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

    def level_up(self):
        """Método para subir de nivel"""
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
            
    def level_up_hability(self, hability):
        """Método para subir de nivel las habilidades"""
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

    def base_stats(self):
        "Método para mostrar estadsticas iniciales"
        base_stats = {
            "Health": self.base_hp,
            "Health Growth": self.base_hp_g,
            "Health Regen": self.base_hp_regen,
            "Health Regen Growth": self.base_hp_regen_g,
            "Mana": self.base_mana,
            "Mana Growth": self.base_mana_g,
            "Mana Regen": self.base_mana_regen,
            "Mana Regen Growth": self.base_mana_regen_g,
            "Energy": self.base_energy,
            "Energy Regen": self.base_energy_regen,
            "Attack Damage": self.base_ad,
            "Attack Damage Growth": self.base_ad_g,
            "Armor": self.base_armor,
            "Armor Growth": self.base_armor_g,
            "Magic Resistance": self.base_mr,
            "Magic Resistance Growth": self.base_mr_g,
            "Range": self.base_range,
            "Movement Speed": self.base_move_speed,
            "Base Attack Speed": self.baseAS,
            "Attack Speed Ratio": self.as_ratio,
            "Bonus Attack Speed": self.bonus_as,
        }
        stats_lines = []
        for stat_name, stat_value in base_stats:
            if stat_value > 0:
                icon_path = stat_icon.get(stat_name, None)
                stats_lines.append({"icon": icon_path, "value": f"{stat_name}: {stat_value}"})
        return stats_lines

    def simple_stats(self):
        """Método para obtener información básica"""
        simple_stats = {
            "Level: ", self.level,
            "Health: ", self.actual_hp,
            "Health Regen: ", self.actual_hp_regen,
            "Mana: ", self.actual_mana,
            "Mana Regen: ", self.actual_mana_regen,
            "Attack Damage: ", self.actual_ad,
            "Attack Speed: ", self.actual_as,
            "Ability Power: ", self.actual_ap,
            "Armor: ", self.actual_total_armor,
            "Magic Resistance: ", self.actual_total_mr,
            "Ability Haste: ", self.actual_ah,
            "Critical Strike Chance(%): ", self.actual_crit_chance,
            "Movement Speed: ", self.actual_move_speed,
        }
        stats_lines = []
        for stat_name, stat_value in simple_stats:
            if stat_value > 0:
                icon_path = stat_icon.get(stat_name, None)
                stats_lines.append({"icon": icon_path, "valye": f"{stat_name}: {stat_value}"})
        return stats_lines

    def extended_stats(self):
        """Método para obtener información extra"""
        extra_stats = {
            "Heal & Shield Power(%)": self.actual_healshield_power,
            "Lethality": self.actual_armorpen_flat,
            "Armor Penetration(%)": self.actual_armorpen_percent,
            "MagicResist Flat Penetration": self.actual_magicpen_flat,
            "MagicResist Penetration(%)": self.actual_magicpen_percent,
            "Lifesteal(%)": self.actual_lifesteal,
            "Range": self.actual_range,
            "Tenacity": self.actual_tenacity,
        }
        stats_lines = []
        for stat_name, stat_value in extra_stats:
            if stat_value > 0:
                icon_path = stat_icon.get(stat_name, None)
                stats_lines.append({"icon": icon_path, "value": f"{stat_name}: {stat_value}"})
        return stats_lines

    def as_peed(self):
        """Método para obtener informacion detallada de la velocidad de ataque"""
        print(f"Actual Attack Speed: {self.actual_as:.3f}")
        print(f"Base Attack Speed: {self.baseAS}")
        print(f"Actual Bonus Attack Speed External: {self.actual_bonus_as_external:.3}")
        print(f"Actual Bonus Attack Speed Leveled: {self.actual_bonus_as_level:.3}")
        print(f"Total Bonus Attack Speed: {math.ceil(self.total_bonus_as * 1000) / 10:.3f}%")
        print(f"Level: {self.level}")
        print(f"Actual Attack Speed Ratio: {self.actual_as_ratio}")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= MÉTODOS RELACIONADOS CON LOS ITEMS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    def add_item(self, item):
        """Método para agregar un item al inventario"""
        for i in range(len(self.items)):
            if self.items[i] is None:
                self.items[i] = item
                self.update_stats(item, add=True)
                print(f"[{self.name}] Item: {item.name} añadido al espacio {i + 1}.")
                return
        print("El inventario está lleno.")

    def remove_item(self, item):
        """Método para eliminar un item del inventario"""
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items[i] = None
                self.update_stats(item, add=False)
                print(f"[{self.name}] Item: {item.name} eliminado del espacio {i + 1}.")
                return
        print("No se encontró el item.")

    def list_items(self):
        """Método para listar los items del inventario"""
        item_list = []
        for i, item in enumerate(self.items):
            if item is not None:
                item_list.append(item.name)
        return item_list

    def update_stats(self, item, add=True):
        """Método para actualizar las estadísticas del campeón despues de agregar o eliminar un item"""
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

    def add_item(self, item):
        """Método para agregar un efecto"""
        for i in range(len(self.items)):
            if self.items[i] is None:
                self.items[i] = item
                self.update_stats(item, add=True)
                print(f"[{self.name}] Item: {item.name} añadido al espacio {i + 1}.")
                return
        print("El inventario está lleno.")

    def remove_item(self, item):
        """Método para eliminar un efecto"""
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items[i] = None
                self.update_stats(item, add=False)
                print(f"[{self.name}] Item: {item.name} eliminado del espacio {i + 1}.")
                return
        print("No se encontró el item.")

    def list_items(self):
        """Método para listar los efectos"""
        item_list = []
        for i, item in enumerate(self.items):
            if item is not None:
                item_list.append(item.name)
        return item_list


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= MÉTODOS RELACIONADOS CON EL COMBATE =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    def sistema_pelea(self, Champion):
        """ Método para el sistema de ataque"""
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

    def realizar_daño(self, enemy):
        """Método donde 2 campeones se pelearán a muerte a base de Auto Ataques"""
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
    
    
    def aa(self, enemy): #self recibe daño de enemy
        """Método para calcular el daño de los AA"""
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
    
            
    
    def hacer_daño(self, cantidad, tipo, Champion):
        """Método para calcular daño dependiento el tipo"""
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
            
    # La idea de éstos métodos es que sea sobre-escritos por los campeones
    def pasiva(self):
        "Método para habilidad pasiva"
        print(f"La pasiva de {self.name} hace efecto")        
            
    def q(self):
        "Método para Q"
        print(f"{self.name} usa Q")
        
    def w(self):
        "Método para W"
        print(f"{self.name} usa W")
        
    def e(self):
        "Método para E"
        print(f"{self.name} usa E")
        
    def r(self):
        "Método para R"
        print(f"{self.name} usa R")    
    