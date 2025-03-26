from ..Champion import Champion

class Aatrox(Champion):
    def __init__(self):
        super().__init__(
            name = "Aatrox",
            title = "The Darkin Blade",
            level = 1,
            base_hp = 650,
            base_hp_g = 114,
            base_hp_regen= 3, 
            base_hp_regen_g = 0.5,
            base_mana = 0,
            base_mana_g = 0,
            base_mana_regen = 0,
            base_mana_regen_g = 0,
            base_energy = 0,
            base_energy_g = 0,
            base_ad = 60,
            base_ad_g = 5,
            base_armor = 38,
            base_armor_g = 4.8,
            base_mr = 32,
            base_mr_g = 2.05,
            base_range = 175,
            base_move_speed = 345,
            base_as = 0.651,
            as_ratio = 0.651,
            bonus_as = 0.025
        )