from Item import Item

class BlackfireTorch (Item):
    def __init__(self):
        super().__init__(
            name = "Blackfire Torch",
            cost = 2800,
            sell = 1960,
            hp = 0,
            hp_regen = 0,
            mana = 600,
            mana_regen = 0,
            ad = 0,
            as_ = 0,
            ap = 80,
            armor = 0,
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
            ah = 20,
            movespeed_flat = 0,
            movespeed_percent = 0
        )