import importlib
import os
import math
from dataclasses import dataclass, field
from Item import Item

CHAMPIONS_FOLDER = "Champions"


    # Método para cargas los campeones
def load_champion(champion_name: str):
    module_name = f"{CHAMPIONS_FOLDER}.{champion_name}"
    try:
        module = importlib.import_module(module_name)
        champ_class = getattr(module, champion_name)
        return champ_class()
    except (ModuleNotFoundError, AttributeError):
        raise ImportError(f"No se encontró el campeón {champion_name} en {module_name}")

    # Método para listar los campeones
def list_champions():
    champions = []
    for filename in os.listdir(CHAMPIONS_FOLDER):
        if filename.endswith(".py") and filename != "__init__.py":
            champions.append(filename[:-3])
    return champions



class Champion:
    name: str
    title: str
    level: int
    its_alive: bool = True

# https://wiki.leagueoflegends.com/en-us/Champion_statistic

    # Valores base del campeón
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
    
    # Valores actuales que se actualizan con subidas de nivel o adquiriendo objetos
    actual_ap: float
    actual_healshield_power: float
    actual_tenacity: float
    actual_slow_resist: float
    actual_crit_chance: float
    actual_crit_damage: float
    actual_armorpen_flat: float
    actual_armorpen_percent: float
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
    # Se calculan despues del constructor con 'def __post_init__()'
    actual_hp: float = field(init=False)
    actual_hp_regen: float = field(init=False)
    actual_mana: float = field(init=False)
    actual_mana_regen: float = field(init=False)
    actual_ad: float = field(init=False)
    actual_armor: float = field(init=False)
    actual_mr: float = field(init=False)
    actual_range: float = field(init=False)
    actual_move_speed: float = field(init=False)
    

    # Constructor
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
        self.__post_init__()

    # Post Constructor
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
        self.actual_armorpen_flat = 0
        self.actual_armorpen_percent = 0
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
        # ¿self.actualGolgGeneration = 0? Idea
        # Iniciación del inventario
        self.items = [None] * 6





    # Método para subir de nivel
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
            self.actual_mr = (self.base_mr + self.base_mr_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            
            # Actualización del crecimiento de la velocidad de ataque por nivel
            self.actual_bonus_as_level += self.as_ratio * self.bonus_as * (0.7025 + 0.0175 * (self.level - 1))
            # Cálculo correcto de la velocidad de ataque con acumulación aditiva
            self.total_bonus_as = self.actual_bonus_as_level + self.actual_bonus_as_external
            self.actual_as = self.baseAS * (1 + self.total_bonus_as)
            
            
            #self.actualAttackSpeed = self.baseAttackSpeed + (self.actualBonusAttackSpeedExternal + self.actualBonusAttackSpeedLeveled * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1))) * self.actualAttackSpeedRatio
        else:
            print("¡Ya has alcanzado el nivel máximo!")

    # Método para obtener información básica
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
        print("Armadura: ", self.actual_armor)
        print("Resistencia Mágica: ", self.actual_mr)
        #velocidad de ataque tehe
        print("Ability Haste: ", self.actual_ah)
        print("Chance de Critico: ", self.actual_crit_chance,"%")
        print("Velocidad de movimiento: ", self.actual_move_speed)


    # Método para obtener información extra
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

    def as_peed(self):
        print(f"Actual Attack Speed: {self.actual_as:.3f}")
        print(f"Base Attack Speed: {self.baseAS}")
        print(f"Actual Bonus Attack Speed External: {self.actual_bonus_as_external:.3}")
        print(f"Actual Bonus Attack Speed Leveled: {self.actual_bonus_as_level:.3}")
        print(f"Total Bonus Attack Speed: {math.ceil(self.total_bonus_as * 1000) / 10:.3f}%")
        print(f"Level: {self.level}")
        print(f"Actual Attack Speed Ratio: {self.actual_as_ratio}")


    # Método para agregar un item al inventario
    def add_item(self, item):
        for i in range(len(self.items)):
            if self.items[i] is None:
                self.items[i] = item
                self.update_stats(item, add=True)
                print(f"[{self.name}] Item: {item.name} añadido al espacio {i + 1}.")
                return
        print("El inventario está lleno.")

    
    # Método para eliminar un item del inventario
    def remove_item(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items[i] = None
                self.update_stats(item, add=False)
                print(f"[{self.name}] Item: {item.name} eliminado del espacio {i + 1}.")
                return
        print("No se encontró el item.")

    
    # Método para listar los items del inventario
    def list_items(self):
        for i, item in enumerate(self.items):
            if item is not None:
                print(f"[{self.name}] Espacio {i + 1}: {item.name}")
            else:
                print(f"[{self.name}] Espacio {i + 1}: Vacío")

    # Método para actualizar las estadísticas del campeón
    def update_stats(self, item, add=True):
        factor = 1 if add else -1
        self.actual_hp += item.hp * factor
        self.actual_hp_regen += item.hp_regen * factor
        self.actual_mana += item.mana * factor
        self.actual_mana_regen += item.mana_regen * factor
        self.actual_ad += item.ad * factor
        self.actual_ap += item.ap * factor
        self.actual_armor += item.armor * factor
        self.actual_mr += item.mr * factor
        self.actual_healthshield_power += item.healshield_power * factor
        self.actual_tenacity += item.tenacity * factor
        self.actual_crit_chance += item.crit_chance * factor
        self.actual_crit_damage += item.crit_damage * factor
        self.actual_armorpen_flat += item.armorpen_flat * factor
        self.actual_armorpen_percent += item.armorpen_percent * factor
        self.actual_magicpen_flat += item.magicpen_flat * factor
        self.actual_magicpen_percent += item.magicpen_percent * factor
        self.actual_lifesteal += item.lifeSteal * factor
        self.actual_ah += item.ah * factor
        self.actual_move_speed += item.movespeed_flat * factor
        self.actual_move_speed += item.movespeed_percent * factor
        self.actual_bonus_as_external += item.as_ * factor
        self.total_bonus_as = self.actual_bonus_as_level + self.actual_bonus_as_external
        self.actual_as = self.baseAS * (1 + self.total_bonus_as)


    # Método para inflingir daño
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
        
        while(self.its_alive and enemy.its_alive == True): # Mientras los dos esten vivos se siguen pegando
            enemy.recibir_daño(self)
            self.recibir_daño(enemy)

            if(enemy.its_alive != True and self.its_alive != True):
                print(f"{self.name} y {enemy.name} murieron")
                break
            elif(enemy.its_alive != True and self.its_alive == True):
                print(f"{enemy.name} fue derrotado por {self.name}")
                break
            elif(enemy.its_alive == True and self.its_alive != True):
                print(f"{self.name} fue derrotado por {enemy.name}")
                break

    # self recibe daño de enemy
    def recibir_daño(self, enemy):
        daño_recibido = max(enemy.actual_ad - self.actual_armor, 0) #Para evitar que el daño sea negativo

        self.actual_hp -= daño_recibido
        print(f"Daño realizado por {enemy.name} hacia {self.name}: {daño_recibido}")
        print(f"Salud de {self.name} actualizado a: {self.actual_hp}")

        if (self.actual_hp <= 0):
            self.its_alive = False

