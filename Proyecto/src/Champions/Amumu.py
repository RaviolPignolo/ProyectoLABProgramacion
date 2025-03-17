from Champion import Champion

class Amumu(Champion):
    def __init__(self):
        super().__init__(
            name = "Amumu",
            title = "The sad mummy",
            level = 1,
            baseHealth = 685,
            baseHealthGrowth = 94,
            baseHealthRegen= 9, 
            baseHealthRegenGrowth = 0.85,
            baseMana = 285,
            baseManaGrowth = 40,
            baseManaRegen = 7.4,
            baseManaRegenGrowth = 0.55,
            baseEnergy = 0,
            baseEnergyRegen = 0,
            baseAttackDamage = 57,
            baseAttackDamageGrowth = 3.8,
            baseArmor = 33,
            baseArmorGrowth = 4,
            baseMagicResist = 32,
            baseMagicResistGrowth = 2.05,
            baseRange = 125,
            baseMoveSpeed = 335,
            baseAttackSpeed = 0.736,
            attackSpeedRatio = 0.638,
            bonusAttackSpeed = 0.0218
        )