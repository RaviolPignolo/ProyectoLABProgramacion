from ..Champion import Champion

class Alistar(Champion):
    def __init__(self):
        super().__init__(
            name = "Alistar",
            title = "The Minotaur",
            level = 1,
            base_hp = 685,
            base_hp_g = 120,
            base_hp_regen= 8.5, 
            base_hp_regen_g = 0.85,
            base_mana = 350,
            base_mana_g = 40,
            base_mana_regen = 8.5,
            base_mana_regen_g = 0.8,
            base_energy = 0,
            base_energy_g = 0,
            base_ad = 62,
            base_ad_g = 3.75,
            base_armor = 47,
            base_armor_g = 4.7,
            base_mr = 32,
            base_mr_g = 2.05,
            base_range = 125,
            base_move_speed = 330,
            base_as = 0.625,
            as_ratio = 0.625,
            bonus_as = 0.02125
        )