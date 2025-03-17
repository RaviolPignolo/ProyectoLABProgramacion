from Champion import Champion

class TahmKench(Champion):
    def __init__(self):
        super().__init__(
            name = "Tahm Kench",
            title = "The River King",
            level = 1,
            baseHealth = 640,
            baseHealthGrowth = 103,
            baseHealthRegen = 6.5,
            baseHealthRegenGrowth = 0.55,
            baseMana = 325,
            baseManaGrowth = 50,
            baseManaRegen = 8,
            baseManaRegenGrowth = 1,
            baseEnergy = 0,
            baseEnergyRegen = 0,
            baseAttackDamage = 56,
            baseAttackDamageGrowth = 3.2,
            baseArmor = 39,
            baseArmorGrowth = 4.7,
            baseMagicResist = 32,
            baseMagicResistGrowth = 2.05,
            baseRange = 175,
            baseMoveSpeed = 335,
            baseAttackSpeed = 0.658,
            attackSpeedRatio = 0.658,
            bonusAttackSpeed = 0.025
        )