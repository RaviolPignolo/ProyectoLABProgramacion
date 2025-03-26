from ..Champion import Champion

class Maokai(Champion):
    def __init__(self):
        super().__init__(
            name = "Maokai",
            title = "The Twisted Treant",
            level = 1,
            base_hp = 665,
            base_hp_g = 109,
            base_hp_regen = 5,
            base_hp_regen_g = 0.75,
            base_mana = 375,
            base_mana_g = 43,
            base_mana_regen = 6,
            base_mana_regen_g = 0.6,
            base_energy = 0,
            base_energy_g = 0,
            base_ad = 64,
            base_ad_g = 3.3,
            base_armor = 35,
            base_armor_g = 5.2,
            base_mr = 32,
            base_mr_g = 2.05,
            base_range = 125,
            base_move_speed = 335,
            base_as = 0.8,
            as_ratio = 0.695,
            bonus_as = 0.02125
        )