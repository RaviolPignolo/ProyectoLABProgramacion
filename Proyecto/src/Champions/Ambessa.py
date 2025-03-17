from Champion import Champion

class Ambessa(Champion):
    def __init__(self):
        super().__init__(
            name = "Ambessa",
            title = "The Matriarch of war",
            level = 1,
            baseHealth = 630,
            baseHealthGrowth = 110,
            baseHealthRegen= 8.5, 
            baseHealthRegenGrowth = 0.75,
            baseMana = 0,
            baseManaGrowth = 0,
            baseManaRegen = 0,
            baseManaRegenGrowth = 0,
            baseEnergy = 200,
            baseEnergyRegen = 50,
            baseAttackDamage = 63,
            baseAttackDamageGrowth = 3,
            baseArmor = 35,
            baseArmorGrowth = 4.9,
            baseMagicResist = 32,
            baseMagicResistGrowth = 2.05,
            baseRange = 125,
            baseMoveSpeed = 335,
            baseAttackSpeed = 0.625,
            attackSpeedRatio = 0.625,
            bonusAttackSpeed = 0.025
        )