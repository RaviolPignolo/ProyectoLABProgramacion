from Champion import Champion

class Maokai(Champion):
    def __init__(self):
        super().__init__(
            name = "Maokai",
            title = "The Twisted Treant",
            level = 1,
            baseHealth = 665,
            baseHealthGrowth = 109,
            baseHealthRegen = 5,
            baseHealthRegenGrowth = 0.75,
            baseMana = 375,
            baseManaGrowth = 43,
            baseManaRegen = 6,
            baseManaRegenGrowth = 0.6,
            baseEnergy = 0,
            baseEnergyRegen = 0,
            baseAttackDamage = 64,
            baseAttackDamageGrowth = 3.3,
            baseArmor = 35,
            baseArmorGrowth = 5.2,
            baseMagicResist = 32,
            baseMagicResistGrowth = 2.05,
            baseRange = 125,
            baseMoveSpeed = 335,
            baseAttackSpeed = 0.8,
            attackSpeedRatio = 0.695,
            bonusAttackSpeed = 0.02125
        )