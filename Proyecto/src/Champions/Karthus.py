from ..Champion import Champion

class Karthus(Champion):
    def __init__(self):
        super().__init__(
            name = "Karthus",
            title = "The Deathsinger",
            level = 1,
            base_hp = 620,
            base_hp_g = 110,
            base_hp_regen= 6.5, 
            base_hp_regen_g = 0.55,
            base_mana = 467,
            base_mana_g = 31,
            base_mana_regen = 8,
            base_mana_regen_g = 0.8,
            base_energy = 0,
            base_energy_g = 0, 
            base_ad = 46,
            base_ad_g = 3.25,
            base_armor = 21,
            base_armor_g = 4.7,
            base_mr = 30,
            base_mr_g = 1.3,
            base_range = 450,
            base_move_speed = 335,
            base_as = 0.625,
            as_ratio = 0.625,
            bonus_as = 0.0211,
        )