from Champion import Champion

class Caitlyn(Champion):
    def __init__(self):
        super().__init__(
            name = "Claitlyn",
            title = "The Sheriff of Piltover",
            level = 1,
            baseHealth = 580,
            baseHealthGrowth = 107,
            baseHealthRegen = 3.5,
            baseHealthRegenGrowth = 0.55,
            baseMana = 315,
            baseManaGrowth = 40,
            baseManaRegen = 7.4,
            baseManaRegenGrowth = 0.7,
            baseEnergy = 0,
            baseEnergyRegen = 0,
            baseAttackDamage = 60,
            baseAttackDamageGrowth = 3.8,
            baseArmor = 27,
            baseArmorGrowth = 4.7,
            baseMagicResist = 30,
            baseMagicResistGrowth = 1.3,
            baseRange = 650,
            baseMoveSpeed = 325,
            baseAttackSpeed = 0.681,
            attackSpeedRatio = 0.625,
            bonusAttackSpeed = 0.04
        )