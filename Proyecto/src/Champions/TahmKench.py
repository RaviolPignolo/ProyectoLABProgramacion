from Champion import Champion

class TahmKench(Champion):
    def __init__(self):
        super().__init__(
            name = "Tahm Kench",
            title = "The River King",
            level = 1,
            base_hp = 640,
            base_hp_g = 103,
            base_hp_regen = 6.5,
            base_hp_regen_g = 0.55,
            base_mana = 325,
            base_mana_g = 50,
            base_mana_regen = 8,
            base_mana_regen_g = 1,
            base_energy = 0,
            base_energy_g = 0,
            base_ad = 56,
            base_ad_g = 3.2,
            base_armor = 39,
            base_armor_g = 4.7,
            base_mr = 32,
            base_mr_g = 2.05,
            base_range = 175,
            base_move_speed = 335,
            base_as = 0.658,
            as_ratio = 0.658,
            bonus_as = 0.025
        )