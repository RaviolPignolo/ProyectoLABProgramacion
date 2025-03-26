from ..Champion import Champion

class Caitlyn(Champion):
    def __init__(self):
        super().__init__(
            name = "Claitlyn",
            title = "The Sheriff of Piltover",
            level = 1,
            base_hp = 580,
            base_hp_g = 107,
            base_hp_regen = 3.5,
            base_hp_regen_g = 0.55,
            base_mana = 315,
            base_mana_g = 40,
            base_mana_regen = 7.4,
            base_mana_regen_g = 0.7,
            base_energy = 0,
            base_energy_g = 0,
            base_ad = 60,
            base_ad_g = 3.8,
            base_armor = 27,
            base_armor_g = 4.7,
            base_mr = 30,
            base_mr_g = 1.3,
            base_range = 650,
            base_move_speed = 325,
            base_as = 0.681,
            as_ratio = 0.625,
            bonus_as = 0.04
        )