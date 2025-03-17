from Champion import Champion

class Aatrox(Champion):
    def __init__(self):
        super().__init__(
            name = "Aatrox",
            title = "The Darkin Blade",
            level = 1,
            baseHealth = 650,
            baseHealthGrowth = 114,
            baseHealthRegen= 3, 
            baseHealthRegenGrowth = 0.5,
            baseMana = 0,
            baseManaGrowth = 0,
            baseManaRegen = 0,
            baseManaRegenGrowth = 0,
            baseEnergy = 0,
            baseEnergyRegen = 0,
            baseAttackDamage = 60,
            baseAttackDamageGrowth = 5,
            baseArmor = 38,
            baseArmorGrowth = 4.8,
            baseMagicResist = 32,
            baseMagicResistGrowth = 2.05,
            baseRange = 175,
            baseMoveSpeed = 345,
            baseAttackSpeed = 0.651,
            attackSpeedRatio = 0.651,
            bonusAttackSpeed = 0.025
        )