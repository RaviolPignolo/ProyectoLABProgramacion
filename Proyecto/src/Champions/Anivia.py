from Champion import Champion

class Anivia(Champion):
    def __init__(self):
        super().__init__(
            name = "Anivia",
            title = "The Cryophoenix",
            level = 1,
            baseHealth = 550,
            baseHealthGrowth = 92,
            baseHealthRegen= 5.5, 
            baseHealthRegenGrowth = 0.55,
            baseMana = 495,
            baseManaGrowth = 45,
            baseManaRegen = 8,
            baseManaRegenGrowth = 0.8,
            baseEnergy = 0,
            baseEnergyRegen = 0,
            baseAttackDamage = 51,
            baseAttackDamageGrowth = 3.2,
            baseArmor = 21,
            baseArmorGrowth = 4.5,
            baseMagicResist = 30,
            baseMagicResistGrowth = 1.3,
            baseRange = 600,
            baseMoveSpeed = 325,
            baseAttackSpeed = 0.658,
            attackSpeedRatio = 0.625,
            bonusAttackSpeed = 0.0168
        )