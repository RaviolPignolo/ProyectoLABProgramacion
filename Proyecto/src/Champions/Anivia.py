from ..Champion import Champion

class Anivia(Champion):
    def __init__(self):
        super().__init__(
            name = "Anivia",
            title = "The Cryophoenix",
            level = 1,
            base_hp = 550,
            base_hp_g = 92,
            base_hp_regen= 5.5, 
            base_hp_regen_g = 0.55,
            base_mana = 495,
            base_mana_g = 45,
            base_mana_regen = 8,
            base_mana_regen_g = 0.8,
            base_energy = 0,
            base_energy_g = 0,
            base_ad = 51,
            base_ad_g = 3.2,
            base_armor = 21,
            base_armor_g = 4.5,
            base_mr = 30,
            base_mr_g = 1.3,
            base_range = 600,
            base_move_speed = 325,
            base_as = 0.658,
            as_ratio = 0.625,
            bonus_as = 0.0168
        )