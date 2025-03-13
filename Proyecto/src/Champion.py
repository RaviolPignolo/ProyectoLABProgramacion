class Champion:
    name: str
    level: int

# https://wiki.leagueoflegends.com/en-us/Champion_statistic

    #Valores base del campeón
    baseHealth: float
    baseHealthGrowth: float
    baseHealthRegen: float
    baseHealthRegenGrowth: float
    baseMana: float
    baseManaGrowth: float
    baseManaRegen: float
    baseManaRegenGrowth: float
    baseAttackDamage: float
    baseAttackDamageGrowth: float
    baseArmor: float
    baseArmorGrowth: float
    baseMagicResist: float
    baseMagicResistGrowth: float

    # Valores actuales que se actualizan con subidas de nivel o adquitiendo objetos
    actualHealth: float
    actualHealthRegen: float
    actualMana: float
    actualManaRegen: float
    actualAttackDamage: float
    actualMagicDamage: float
    actualArmor: float
    actualMagicResist: float

    ### faltas stats

    # Constructor
    def __init__(self, name, level, baseHealth, baseHealthGrowth, baseHealthRegen, baseHealthRegenGrowth, baseMana, baseManaGrowth, baseManaRegen, baseManaRegenGrowth, baseAttackDamage, baseAttackDamageGrowth, baseArmor, baseArmorGrowth, baseMagicResist, baseMagicResistGrowth):
        self.name = name
        self.level = level
        self.baseHealth = baseHealth
        self.baseHealthGrowth = baseHealthGrowth
        self.baseHealthRegen = baseHealthRegen
        self.baseHealthRegenGrowth = baseHealthRegenGrowth
        self.baseMana = baseMana
        self.baseManaGrowth = baseManaGrowth
        self.baseManaRegen = baseManaRegen
        self.baseManaRegenGrowth = baseManaRegenGrowth
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
        self.actualMagicDamage = 0
        self.actualArmor = baseArmor
        self.actualMagicResist = baseMagicResist
    
    # Método para subir de nivel
    def level_up(self):
        if(self.level <= 18):
            self.level += 1
            self.actualHealth = (self.baseHealth + self.baseHealthGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actualHealthRegen = (self.baseHealthRegen + self.baseHealthRegenGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actualMana = (self.baseMana + self.baseManaGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actualManaRegen = (self.baseManaRegen + self.baseManaRegenGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actualAttackDamage = (self.baseAttackDamage + self.baseAttackDamageGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actualArmor = (self.baseArmor + self.baseArmorGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actualMagicResist = (self.baseMagicResist + self.baseMagicResistGrowth * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            print("////////// LEVEL UP! \\\\\\\\\\")
        else:
            print("¡Ya has alcanzado el nivel máximo!")

    # Método para obtener información reducida
    def simple_stats(self):
        return f"Nivel: {self.level} \nSalud: {self.actualHealth} \nRegeneración de salud: {self.actualHealthRegen} \nMana: {self.actualMana} \nRegeneración de mana: {self.actualManaRegen} \nAD: {self.actualAttackDamage} \nAP: {self.actualMagicDamage} \nArmadura: {self.actualArmor} \nResistencia mágica: {self.actualMagicResist}"
    
    # Método para obtener información extendida
    def extended_stats(self):
        return f"Nivel: {self.level} \nSalud: {self.actualHealth} \nRegeneración de Salud: {self.actualHealthRegen} \nMana: {self.actualMana} \nRegeneración de Mana: {self.actualManaRegen} \nAD: {self.actualAttackDamage} \nAP: {self.actualMagicDamage} \nArmadura: {self.actualArmor} \nResistencia Mágica: {self.actualMagicResist}"



Karthus = Champion("Karthus", 1, 620, 110, 6.5, 0.55, 467, 31, 8, 0.8, 46, 3.25, 21, 4.7, 30, 1.3)

print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())
Karthus.level_up()
print(Karthus.simple_stats())