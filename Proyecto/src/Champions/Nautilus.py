from Champion import Champion

class Nautilus(Champion):
    def __init__(self):
        super().__init__(
            name = "Nautilus",
            title = "The Titan of the depths",
            level = 1,
            base_hp = 646,
            base_hp_g = 100,
            base_hp_regen = 8.5,
            base_hp_regen_g = 0.55,
            base_mana = 400,
            base_mana_g = 47,
            base_mana_regen = 8.65,
            base_mana_regen_g = 0.5,
            base_energy = 0,
            base_energy_g = 0,
            base_ad = 61,
            base_ad_g = 3.3,
            base_armor = 39,
            base_armor_g = 4.95,
            base_mr = 32,
            base_mr_g = 2.05,
            base_range = 175,
            base_move_speed = 325,
            base_as = 0.706,
            as_ratio = 0.612,
            bonus_as = 0.01
        )