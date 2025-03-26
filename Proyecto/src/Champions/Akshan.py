from ..Champion import Champion

class Akshan(Champion):
    def __init__(self):
        super().__init__(
            name = "Akshan",
            title = "The Rogue Sentinel",
            level = 1,
            base_hp = 630,
            base_hp_g = 107,
            base_hp_regen= 3.75, 
            base_hp_regen_g = 0.65,
            base_mana = 350,
            base_mana_g = 40,
            base_mana_regen = 8.2,
            base_mana_regen_g = 0.7,
            base_energy = 0,
            base_energy_g = 0,
            base_ad = 52,
            base_ad_g = 3,
            base_armor = 26,
            base_armor_g = 4.7,
            base_mr = 30,
            base_mr_g = 1.3,
            base_range = 500,
            base_move_speed = 330,
            base_as = 0.638,
            as_ratio = 0.4,
            bonus_as = 0.04
        )