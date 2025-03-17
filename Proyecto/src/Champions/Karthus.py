from Champion import Champion

class Karthus(Champion):
    def __init__(self):
        super().__init__(
            name = "Karthus",
            title = "The Deathsinger",
            level = 1,
            baseHealth = 620,
            baseHealthGrowth = 110,
            baseHealthRegen= 6.5, 
            baseHealthRegenGrowth = 0.55,
            baseMana = 467,
            baseManaGrowth = 31,
            baseManaRegen = 8,
            baseManaRegenGrowth = 0.8,
            baseEnergy = 0,
            baseEnergyRegen = 0, 
            baseAttackDamage = 46,
            baseAttackDamageGrowth = 3.25,
            baseArmor = 21,
            baseArmorGrowth = 4.7,
            baseMagicResist = 30,
            baseMagicResistGrowth = 1.3,
            baseRange = 450,
            baseMoveSpeed = 335,
            baseAttackSpeed = 0.625,
            attackSpeedRatio = 0.625,
            bonusAttackSpeed = 0.0211,
        )