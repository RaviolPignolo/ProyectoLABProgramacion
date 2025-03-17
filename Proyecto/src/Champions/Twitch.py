from Champion import Champion

class Twitch(Champion):
    def __init__(self):
        super().__init__(
            name = "Twitch",
            title = "The Plague Rat",
            level = 1,
            baseHealth = 630,
            baseHealthGrowth = 104,
            baseHealthRegen = 3.75,
            baseHealthRegenGrowth = 0.6,
            baseMana = 300,
            baseManaGrowth = 40,
            baseManaRegen = 7.25,
            baseManaRegenGrowth = 0.7,
            baseEnergy = 0,
            baseEnergyRegen = 0,
            baseAttackDamage = 59,
            baseAttackDamageGrowth = 3.1,
            baseArmor = 27,
            baseArmorGrowth = 4.2,
            baseMagicResist = 30,
            baseMagicResistGrowth = 1.3,
            baseRange = 550,
            baseMoveSpeed = 330,
            baseAttackSpeed = 0.679,
            attackSpeedRatio = 0.679,
            bonusAttackSpeed = 0.0338
        )