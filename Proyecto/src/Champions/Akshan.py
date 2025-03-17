from Champion import Champion

class Akshan(Champion):
    def __init__(self):
        super().__init__(
            name = "Akshan",
            title = "The Rogue Sentinel",
            level = 1,
            baseHealth = 630,
            baseHealthGrowth = 107,
            baseHealthRegen= 3.75, 
            baseHealthRegenGrowth = 0.65,
            baseMana = 350,
            baseManaGrowth = 40,
            baseManaRegen = 8.2,
            baseManaRegenGrowth = 0.7,
            baseEnergy = 0,
            baseEnergyRegen = 0,
            baseAttackDamage = 52,
            baseAttackDamageGrowth = 3,
            baseArmor = 26,
            baseArmorGrowth = 4.7,
            baseMagicResist = 30,
            baseMagicResistGrowth = 1.3,
            baseRange = 500,
            baseMoveSpeed = 330,
            baseAttackSpeed = 0.638,
            attackSpeedRatio = 0.4,
            bonusAttackSpeed = 0.04
        )