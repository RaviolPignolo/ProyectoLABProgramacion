from Item import Item

        #### Abilidades WIP ####

class Champion:
    name: str
    title: str
    level: int
    itsAlive: bool = True

# https://wiki.leagueoflegends.com/en-us/Champion_statistic

    #Valores base del campeón que tienen escalado por nivel
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

    # Valores actuales que se actualizan con subidas de nivel o adquiriendo objetos
    actualHealth: float
    actualHealthRegen: float
    actualMana: float
    actualManaRegen: float
    actualAttackDamage: float
    actualAbilityPower: float
    actualArmor: float
    actualMagicResist: float
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

    # Constructor
    def __init__(self, name, title, level, baseHealth, baseHealthGrowth, baseHealthRegen, baseHealthRegenGrowth, baseMana, baseManaGrowth, baseManaRegen, baseManaRegenGrowth, baseEnergy, baseEnergyRegen, baseAttackDamage, baseAttackDamageGrowth, baseArmor, baseArmorGrowth, baseMagicResist, baseMagicResistGrowth, baseRange, baseMoveSpeed):
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
        self.actualHealth = baseHealth
        self.actualHealthRegen = baseHealthRegen
        self.actualMana = baseMana
        self.actualManaRegen = baseManaRegen
        self.actualAttackDamage = baseAttackDamage
        self.actualArmor = baseArmor
        self.actualMagicResist = baseMagicResist
        self.actualRange = baseRange
        self.actualMoveSpeed = baseMoveSpeed
        # Estadisticas obtenibles de forma externa (items, runas, etc)
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
        else:
            print("¡Ya has alcanzado el nivel máximo!")

    # Método para obtener información básica
    def simple_stats(self):
        print("Nivel: ", self.level)
        print("Salud: ", self.actualHealth)
        print("Regeneración de Salud: ", self.actualHealthRegen)
        print("Mana: ", self.actualMana)
        print("Regeneración de Mana: ", self.actualManaRegen)
        print("AD: ", self.actualAttackDamage)
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
                print(f"[{self.name}] Item: {item.name} añadido al espacio {i + 1}.")
                return
        print("El inventario está lleno.")

    
    # Método para eliminar un item del inventario
    def remove_item(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items[i] = None
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