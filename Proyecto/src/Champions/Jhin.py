from Champion import Champion

class Jhin(Champion):
    def __init__(self):
        super().__init__(
            name = "Jhin",
            title = "The Virtuoso",
            level = 1,
            baseHealth = 655,
            baseHealthGrowth = 107,
            baseHealthRegen = 3.75,
            baseHealthRegenGrowth = 0.55,
            baseMana = 300,
            baseManaGrowth = 50,
            baseManaRegen = 6,
            baseManaRegenGrowth = 0.8,
            baseEnergy = 0,
            baseEnergyRegen = 0,
            baseAttackDamage = 59,
            baseAttackDamageGrowth = 4.4,
            baseArmor = 24,
            baseArmorGrowth = 4.7,
            baseMagicResist = 30,
            baseMagicResistGrowth = 1.3,
            baseRange = 550,
            baseMoveSpeed = 300,
            baseAttackSpeed = 0.625,
            attackSpeedRatio = 0,
            bonusAttackSpeed = 0
        )