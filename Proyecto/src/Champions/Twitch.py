from ..Champion import Champion

class Twitch(Champion):
    def __init__(self):
        super().__init__(
            name = "Twitch",
            title = "The Plague Rat",
            level = 1,
            base_hp = 630,
            base_hp_g = 104,
            base_hp_regen = 3.75,
            base_hp_regen_g = 0.6,
            base_mana = 300,
            base_mana_g = 40,
            base_mana_regen = 7.25,
            base_mana_regen_g = 0.7,
            base_energy = 0,
            base_energy_g = 0,
            base_ad = 59,
            base_ad_g = 3.1,
            base_armor = 27,
            base_armor_g = 4.2,
            base_mr = 30,
            base_mr_g = 1.3,
            base_range = 550,
            base_move_speed = 330,
            base_as = 0.679,
            as_ratio = 0.679,
            bonus_as = 0.0338
        )