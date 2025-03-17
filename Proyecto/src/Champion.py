import importlib
import os
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
    itsAlive: bool = True

# https://wiki.leagueoflegends.com/en-us/Champion_statistic

    # Valores base del campeón
    baseHealth: float
    baseHealthGrowth: float
    baseHealthRegen: float
    baseHealthRegenGrowth: float
    baseMana: float
    baseManaGrowth: float
    baseManaRegen: float
    baseManaRegenGrowth: float
    baseEnergy: float
    baseEnergyRegen: float
    baseAttackDamage: float
    baseAttackDamageGrowth: float
    baseArmor: float
    baseArmorGrowth: float
    baseMagicResist: float
    baseMagicResistGrowth: float
    baseRange: float
    baseMoveSpeed: float
    baseAttackSpeed: float
    
    # Valores actuales que se actualizan con subidas de nivel o adquiriendo objetos
    actualAbilityPower: float
    actualHealShieldPower: float
    actualTenacity: float
    actualSlowResist: float
    actualCriticalStrikeChance: float
    actualCriticalStrikeDamage: float
    actualArmorPenetrationFlat: float
    actualArmorPenetrationPercent: float
    actualMagicPenetrationFlat: float
    actualMagicPenetrationPercent: float
    actualLifeSteal: float
    actualPhysicalVamp: float
    actualOmnivamp: float
    actualAbilityHaste: float
    attackSpeedRatio: float
    bonusAttackSpeed: float
    actualAttackSpeed: float
    actualAttackSpeedRatio: float
    actualBonusAttackSpeedLeveled: float
    actualBonusAttackSpeedExternal: float
    # Se calculan despues del constructor con 'def __post_init__()'
    actualHealth: float = field(init=False)
    actualHealthRegen: float = field(init=False)
    actualMana: float = field(init=False)
    actualManaRegen: float = field(init=False)
    actualAttackDamage: float = field(init=False)
    actualArmor: float = field(init=False)
    actualMagicResist: float = field(init=False)
    actualRange: float = field(init=False)
    actualMoveSpeed: float = field(init=False)
    

    # Constructor
    def __init__(self,
                 name, title, level,
                 baseHealth, baseHealthGrowth,
                 baseHealthRegen, baseHealthRegenGrowth,
                 baseMana, baseManaGrowth,
                 baseManaRegen, baseManaRegenGrowth,
                 baseEnergy, baseEnergyRegen,
                 baseAttackDamage, baseAttackDamageGrowth,
                 baseArmor, baseArmorGrowth,
                 baseMagicResist, baseMagicResistGrowth,
                 baseRange, baseMoveSpeed,
                 baseAttackSpeed, attackSpeedRatio, bonusAttackSpeed):
        self.name = name
        self.title = title
        self.level = level
        self.baseHealth = baseHealth
        self.baseHealthGrowth = baseHealthGrowth
        self.baseHealthRegen = baseHealthRegen
        self.baseHealthRegenGrowth = baseHealthRegenGrowth
        self.baseMana = baseMana
        self.baseManaGrowth = baseManaGrowth
        self.baseManaRegen = baseManaRegen
        self.baseManaRegenGrowth = baseManaRegenGrowth
        self.baseEnergy = baseEnergy
        self.baseEnergyRegen = baseEnergyRegen
        self.baseAttackDamage = baseAttackDamage
        self.baseAttackDamageGrowth = baseAttackDamageGrowth
        self.baseArmor = baseArmor
        self.baseArmorGrowth = baseArmorGrowth
        self.baseMagicResist = baseMagicResist
        self.baseMagicResistGrowth = baseMagicResistGrowth
        self.baseRange = baseRange
        self.baseMoveSpeed = baseMoveSpeed
        self.baseAttackSpeed = baseAttackSpeed
        self.attackSpeedRatio = attackSpeedRatio
        self.bonusAttackSpeed = bonusAttackSpeed
        self.__post_init__()

    # Post Constructor
    def __post_init__(self):
        self.actualHealth = self.baseHealth
        self.actualHealthRegen = self.baseHealthRegen
        self.actualMana = self.baseMana
        self.actualManaRegen = self.baseManaRegen
        self.actualAttackDamage = self.baseAttackDamage
        self.actualArmor = self.baseArmor
        self.actualMagicResist = self.baseMagicResist
        self.actualRange = self.baseRange
        self.actualMoveSpeed = self.baseMoveSpeed
        self.actualHealShieldPower = 0
        self.actualTenacity = 0
        self.actualSlowResist = 0
        self.actualAbilityPower = 0
        self.actualCriticalStrikeChance = 0
        self.actualCriticalStrikeDamage = 0
        self.actualArmorPenetrationFlat = 0
        self.actualArmorPenetrationPercent = 0
        self.actualMagicPenetrationFlat = 0
        self.actualMagicPenetrationPercent = 0
        self.actualLifeSteal = 0
        self.actualPhysicalVamp = 0
        self.actualOmnivamp = 0
        self.actualAbilityHaste = 0
        self.actualAttackSpeed = self.baseAttackSpeed
        self.actualAttackSpeedRatio = self.attackSpeedRatio
        self.actualBonusAttackSpeedLeveled = 0
        self.actualBonusAttackSpeedExternal = 0
        # ¿self.actualGolgGeneration = 0? Idea
        # Iniciación del inventario
        self.items = [None] * 6





    # Método para subir de nivel
    def level_up(self):
        if self.level < 18:
            print("////////// LEVEL UP! \\\\\\\\\\")
            self.level += 1
            self.actualHealth = (self.baseHealth + self.baseHealthGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actualHealthRegen = (self.baseHealthRegen + self.baseHealthRegenGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actualMana = (self.baseMana + self.baseManaGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actualManaRegen = (self.baseManaRegen + self.baseManaRegenGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actualAttackDamage = (self.baseAttackDamage + self.baseAttackDamageGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actualArmor = (self.baseArmor + self.baseArmorGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actualMagicResist = (self.baseMagicResist + self.baseMagicResistGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            
            self.actualAttackSpeed = self.baseAttackSpeed + (self.actualBonusAttackSpeedExternal + self.actualBonusAttackSpeedLeveled * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1))) * self.actualAttackSpeedRatio
        else:
            print("¡Ya has alcanzado el nivel máximo!")

    '''
    Matemática para la subida de nivel
    Citando:
    https://wiki.leagueoflegends.com/en-us/Champion_statistic#Increasing_Statistics

    To calculate a champion's statistics at a specific level, the following formula is used:

                Statistic = base + bonus + g * (n-1) * (0.7025 + 0.0175 * (n - 1))
    
    - base = initial statistic value
    - bonus = bonus statistic from any source (runes, items, buffs, etc.)
    - g = growth statistic
    - n = current champion level
    - (n - 1) = total number of level ups


    https://wiki.leagueoflegends.com/en-us/Champion_statistic#Attack_speed_calculations
    
    Attack speed uses different types of values, instead of simply a base and a growth amount:

    Base attack speed
    - Attack speed ratio, which may be the same value as the base attack speed or a different one, depending on the champion
    - Bonus attack speed growth, as a percentage (%)
    - Bonus attack speed from other sources, as a percentage (%)

    Because of the facts that:
        1) The base and ratio values are functionally unchanging, and the ratio is a multiplier for all attack speed gained
        2) Attack speed increases in percentages
        3) Attack speed gained through levels is considered different from attack speed gained through any other source, but they are both added together as "bonus attack speed"

        The above statistic formula must be adjusted.

                TotalAttackSpeed = baseAS + [bonusAS + g * (n - 1) * (0.7025 + 0.0175 * (n - 1))] * ASratio
        
    - baseAS = base attack speed
    - ASratio = attack speed ratio, if different from base attack speed; otherwise, replace with baseAs
    - g = percent bonus attack speed growth, gained explicitly from leveling up
    - bonusAS = sum of any percent bonus attack speed gained explicitly from any source except leveling up
    - n = current champion level
    - (n - 1) = total number of level ups
    '''


    # Método para obtener información básica
    def simple_stats(self):
        print("Campeón: ", self.name)
        print("Nivel: ", self.level)
        print("Salud: ", self.actualHealth)
        print("Regeneración de Salud: ", self.actualHealthRegen)
        print("Mana: ", self.actualMana)
        print("Regeneración de Mana: ", self.actualManaRegen)
        print("AD: ", self.actualAttackDamage)
        print("AS: ", self.actualAttackSpeed, "%")
        print("AP: ", self.actualAbilityPower)
        print("Armadura: ", self.actualArmor)
        print("Resistencia Mágica: ", self.actualMagicResist)
        #velocidad de ataque tehe
        print("Ability Haste: ", self.actualAbilityHaste)
        print("Chance de Critico: ", self.actualCriticalStrikeChance,"%")
        print("Velocidad de movimiento: ", self.actualMoveSpeed)


    # Método para obtener información extra
    def extended_stats(self):
        ## health | resource regeneration ¿?¿?¿?
        print("Poder de Curaciones y Escudos: ", self.actualHealShieldPower,"%")
        print("Letalidad: ", self.actualArmorPenetrationFlat)
        print("Penetración de Armadura porcentual: ", self.actualArmorPenetrationPercent,"%")
        print("Penetración de Resistencia Mágica plana: ", self.actualMagicPenetrationFlat)
        print("Penetración de Resistencia Mágica porcentual: ", self.actualMagicPenetrationPercent,"%")
        print("Robo de Vida: ", self.actualLifeSteal,"%")
        print("Vampirismo: ", self.actualOmnivamp,"%")
        print("Rango de ataque: ", self.actualRange)
        print("Tenacidad: ", self.actualTenacity,"%")


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
        self.actualHealth += item.health * factor
        self.actualHealthRegen += item.healthRegen * factor
        self.actualMana += item.mana * factor
        self.actualManaRegen += item.manaRegen * factor
        self.actualAttackDamage += item.attackDamage * factor
        self.actualAbilityPower += item.abilityPower * factor
        self.actualArmor += item.armor * factor
        self.actualMagicResist += item.magicResist * factor
        self.actualHealShieldPower += item.healShieldPower * factor
        self.actualTenacity += item.tenacity * factor
        self.actualCriticalStrikeChance += item.criticalStrikeChance * factor
        self.actualCriticalStrikeDamage += item.criticalStrikeDamage * factor
        self.actualArmorPenetrationFlat += item.armorPenetrationFlat * factor
        self.actualArmorPenetrationPercent += item.armorPenetrationPercent * factor
        self.actualMagicPenetrationFlat += item.magicPenetrationFlat * factor
        self.actualMagicPenetrationPercent += item.magicPenetrationPercent * factor
        self.actualLifeSteal += item.lifeSteal * factor
        self.actualAbilityHaste += item.abilityHaste * factor
        self.actualMoveSpeed += item.moveSpeedFlat * factor
        self.actualMoveSpeed += item.moveSpeed * factor
        self.actualBonusAttackSpeedExternal += item.attackSpeed * factor
        


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
        
        while(self.itsAlive and enemy.itsAlive == True): # Mientras los dos esten vivos se siguen pegando
            enemy.recibir_daño(self)
            self.recibir_daño(enemy)

            if(enemy.itsAlive != True and self.itsAlive != True):
                print(f"{self.name} y {enemy.name} murieron")
                break
            elif(enemy.itsAlive != True and self.itsAlive == True):
                print(f"{enemy.name} fue derrotado por {self.name}")
                break
            elif(enemy.itsAlive == True and self.itsAlive != True):
                print(f"{self.name} fue derrotado por {enemy.name}")
                break

    # self recibe daño de enemy
    def recibir_daño(self, enemy):
        daño_recibido = max(enemy.actualAttackDamage - self.actualArmor, 0) #Para evitar que el daño sea negativo

        self.actualHealth -= daño_recibido
        print(f"Daño realizado por {enemy.name} hacia {self.name}: {daño_recibido}")
        print(f"Salud de {self.name} actualizado a: {self.actualHealth}")

        if (self.actualHealth <= 0):
            self.itsAlive = False

