from Champion import Champion

class Akali(Champion):
    def __init__(self):
        super().__init__(
            name = "Akali",
            title = "The Rogue Assassin",
            level = 1,
            baseHealth = 600,
            baseHealthGrowth = 119,
            baseHealthRegen= 9, 
            baseHealthRegenGrowth = 0.9,
            baseMana = 0,
            baseManaGrowth = 0,
            baseManaRegen = 0,
            baseManaRegenGrowth = 0,
            baseEnergy = 200,
            baseEnergyRegen = 50,
            baseAttackDamage = 62,
            baseAttackDamageGrowth = 3.3,
            baseArmor = 23,
            baseArmorGrowth = 4.7,
            baseMagicResist = 37,
            baseMagicResistGrowth = 2.05,
            baseRange = 125,
            baseMoveSpeed = 345,
            baseAttackSpeed = 0.625,
            attackSpeedRatio = 0.625,
            bonusAttackSpeed = 0.032
        )