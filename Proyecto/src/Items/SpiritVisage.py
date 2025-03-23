from Item import Item

class SpiritVisage (Item):
    def __init__(self):
        super().__init__(
            name = "Spirit Visage",
            cost = 2700,
            sell = 1890,
            hp = 400,
            hp_regen = 1.00, # 100%
            mana = 0,
            mana_regen = 0,
            ad = 0,
            as_ = 0,
            ap = 0,
            armor = 0,
            mr = 50,
            healshield_power = 0,
            tenacity = 0,
            crit_chance = 0,
            crit_damage = 0,
            armorpen_flat = 0,
            armorpen_percent = 0,
            magicpen_flat = 0,
            magicpen_percent = 0,
            lifesteal = 0,
            ah = 10,
            movespeed_flat = 0,
            movespeed_percent = 0
        )