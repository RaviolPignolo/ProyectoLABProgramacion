from Champion import Champion

class Alistar(Champion):
    def __init__(self):
        super().__init__(
            name = "Alistar",
            title = "The Minotaur",
            level = 1,
            baseHealth = 685,
            baseHealthGrowth = 120,
            baseHealthRegen= 8.5, 
            baseHealthRegenGrowth = 0.85,
            baseMana = 350,
            baseManaGrowth = 40,
            baseManaRegen = 8.5,
            baseManaRegenGrowth = 0.8,
            baseEnergy = 0,
            baseEnergyRegen = 0,
            baseAttackDamage = 62,
            baseAttackDamageGrowth = 3.75,
            baseArmor = 47,
            baseArmorGrowth = 4.7,
            baseMagicResist = 32,
            baseMagicResistGrowth = 2.05,
            baseRange = 125,
            baseMoveSpeed = 330,
            baseAttackSpeed = 0.625,
            attackSpeedRatio = 0.625,
            bonusAttackSpeed = 0.02125
        )