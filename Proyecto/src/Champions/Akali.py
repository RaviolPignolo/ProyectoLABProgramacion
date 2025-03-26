from ..Champion import Champion

class Akali(Champion):
    def __init__(self):
        super().__init__(
            name = "Akali",
            title = "The Rogue Assassin",
            level = 1,
            base_hp = 600,
            base_hp_g = 119,
            base_hp_regen= 9, 
            base_hp_regen_g = 0.9,
            base_mana = 0,
            base_mana_g = 0,
            base_mana_regen = 0,
            base_mana_regen_g = 0,
            base_energy = 200,
            base_energy_g = 50,
            base_ad = 62,
            base_ad_g = 3.3,
            base_armor = 23,
            base_armor_g = 4.7,
            base_mr = 37,
            base_mr_g = 2.05,
            base_range = 125,
            base_move_speed = 345,
            base_as = 0.625,
            as_ratio = 0.625,
            bonus_as = 0.032
        )