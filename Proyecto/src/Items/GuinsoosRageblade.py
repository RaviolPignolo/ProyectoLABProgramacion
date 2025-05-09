from ..Item import Item

class GuinsoosRageblade (Item):
    def __init__(self):
        super().__init__(
            name = "Guinsoo's Rageblade",
            cost = 3000,
            sell = 2100,
            hp = 0,
            hp_regen = 0,
            mana = 0,
            mana_regen = 0,
            ad = 30,
            as_ = 0.25, # 25%
            ap = 30,
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
            ah = 0,
            movespeed_flat = 0,
            movespeed_percent = 0
        )