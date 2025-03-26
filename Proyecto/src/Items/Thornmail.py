from ..Item import Item

class Thornmail (Item):
    def __init__(self):
        super().__init__(
            name = "Thornmail",
            cost = 2450,
            sell = 1715,
            hp = 150,
            hp_regen = 0,
            mana = 0,
            mana_regen = 0,
            ad = 0,
            as_ = 0,
            ap = 0,
            armor = 75,
            mr = 0,
            healshield_power = 0,
            tenacity = 0,
            crit_chance = 0,
            crit_damage = 0,
            armorpen_flat = 0,
            armorpen_percent = 0,
            magicpen_flat = 0,
            magicpen_percent = 0,
            lifesteal = 0,
            ah = 0,
            movespeed_flat = 0,
            movespeed_percent = 0
        )