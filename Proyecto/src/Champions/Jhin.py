from Champion import Champion

class Jhin(Champion):
    def __init__(self):
        super().__init__(
            name = "Jhin",
            title = "The Virtuoso",
            level = 1,
            base_hp = 655,
            base_hp_g = 107,
            base_hp_regen = 3.75,
            base_hp_regen_g = 0.55,
            base_mana = 300,
            base_mana_g = 50,
            base_mana_regen = 6,
            base_mana_regen_g = 0.8,
            base_energy = 0,
            base_energy_g = 0,
            base_ad = 59,
            base_ad_g = 4.4,
            base_armor = 24,
            base_armor_g = 4.7,
            base_mr = 30,
            base_mr_g = 1.3,
            base_range = 550,
            base_move_speed = 300,
            base_as = 0.625,
            as_ratio = 0,
            bonus_as = 0
        )