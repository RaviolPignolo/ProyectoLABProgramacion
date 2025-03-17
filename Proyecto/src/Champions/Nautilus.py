from Champion import Champion

class Nautilus(Champion):
    def __init__(self):
        super().__init__(
            name = "Nautilus",
            title = "The Titan of the depths",
            level = 1,
            baseHealth = 646,
            baseHealthGrowth = 100,
            baseHealthRegen = 8.5,
            baseHealthRegenGrowth = 0.55,
            baseMana = 400,
            baseManaGrowth = 47,
            baseManaRegen = 8.65,
            baseManaRegenGrowth = 0.5,
            baseEnergy = 0,
            baseEnergyRegen = 0,
            baseAttackDamage = 61,
            baseAttackDamageGrowth = 3.3,
            baseArmor = 39,
            baseArmorGrowth = 4.95,
            baseMagicResist = 32,
            baseMagicResistGrowth = 2.05,
            baseRange = 175,
            baseMoveSpeed = 325,
            baseAttackSpeed = 0.706,
            attackSpeedRatio = 0.612,
            bonusAttackSpeed = 0.01
        )