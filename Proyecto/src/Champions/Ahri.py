from Champion import Champion

class Ahri(Champion):
    def __init__(self):
        super().__init__(
            name = "Ahri",
            title = "The Nine-Tailed Fox",
            level = 1,
            base_hp = 590,
            base_hp_g = 104,
            base_hp_regen= 2.5, 
            base_hp_regen_g = 0.6,
            base_mana = 418,
            base_mana_g = 25,
            base_mana_regen = 8,
            base_mana_regen_g = 0.8,
            base_energy = 0,
            base_energy_g = 0,
            base_ad = 53,
            base_ad_g = 3,
            base_armor = 21,
            base_armor_g = 4.7,
            base_mr = 30,
            base_mr_g = 1.3,
            base_range = 550,
            base_move_speed = 330,
            base_as = 0.668,
            as_ratio = 0.625,
            bonus_as = 0.022
        )