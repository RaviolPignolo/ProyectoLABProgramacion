from Champion import Champion

class Ahri(Champion):
    def __init__(self):
        super().__init__(
            name = "Ahri",
            title = "The Nine-Tailed Fox",
            level = 1,
            baseHealth = 590,
            baseHealthGrowth = 104,
            baseHealthRegen= 2.5, 
            baseHealthRegenGrowth = 0.6,
            baseMana = 418,
            baseManaGrowth = 25,
            baseManaRegen = 8,
            baseManaRegenGrowth = 0.8,
            baseEnergy = 0,
            baseEnergyRegen = 0,
            baseAttackDamage = 53,
            baseAttackDamageGrowth = 3,
            baseArmor = 21,
            baseArmorGrowth = 4.7,
            baseMagicResist = 30,
            baseMagicResistGrowth = 1.3,
            baseRange = 550,
            baseMoveSpeed = 330,
            baseAttackSpeed = 0.668,
            attackSpeedRatio = 0.625,
            bonusAttackSpeed = 0.022
        )