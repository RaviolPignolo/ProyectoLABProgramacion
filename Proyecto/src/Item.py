import importlib
import os

ITEM_FOLDER = "Proyecto.src.Items" # Carpeta que contiene los items

stat_icon = { # Ubicación de los iconos correspondientes a las estadisticas
    "Gold": "Proyecto/src/Assets/Images/StatIcon/Gold_icon.png",
    "Health": "Proyecto/src/Assets/Images/StatIcon/Health_icon.png",
    "Health Regen(%)": "Proyecto/src/Assets/Images/StatIcon/Health_regeneration_icon.png",
    "Mana": "Proyecto/src/Assets/Images/StatIcon/Mana_icon.png",
    "Mana Regen(%)": "Proyecto/src/Assets/Images/StatIcon/Mana_regeneration_icon.png",
    "Attack Damage": "Proyecto/src/Assets/Images/StatIcon/Attack_damage_icon.png",
    "Ability Power": "Proyecto/src/Assets/Images/StatIcon/Ability_power_icon.png",
    "Attack Speed(%)": "Proyecto/src/Assets/Images/StatIcon/Attack_speed_icon.png",
    "Armor": "Proyecto/src/Assets/Images/StatIcon/Armor_icon.png",
    "Magic Resistance": "Proyecto/src/Assets/Images/StatIcon/Magic_resistance_icon.png",
    "Heal & shield power(%)": "Proyecto/src/Assets/Images/StatIcon/Heal_and_shield_power_icon.png",
    "Tenacity": "Proyecto/src/Assets/Images/StatIcon/Tenacity_icon.png",
    "Critical strike chance(%)": "Proyecto/src/Assets/Images/StatIcon/Critical_strike_chance_icon.png",
    "Critical strike damage(%)": "Proyecto/src/Assets/Images/StatIcon/Critical_strike_damage_icon.png",
    "Lethality": "Proyecto/src/Assets/Images/StatIcon/Armor_penetration_icon.png",
    "Armor penetration(%)": "Proyecto/src/Assets/Images/StatIcon/Armor_penetration_icon.png",
    "MagicResist flat penetration": "Proyecto/src/Assets/Images/StatIcon/Magic_penetration_icon.png",
    "MagicResist penetration(%)": "Proyecto/src/Assets/Images/StatIcon/Magic_penetration_icon.png",
    "Lifesteal(%)": "Proyecto/src/Assets/Images/StatIcon/Life_steal_icon.png",
    "Ability haste": "Proyecto/src/Assets/Images/StatIcon/Cooldown_reduction_icon.png",
    "Movement Speed": "Proyecto/src/Assets/Images/StatIcon/Movement_speed_icon.png",
    "Movement Speed(%)": "Proyecto/src/Assets/Images/StatIcon/Movement_speed_icon.png",
}

# Éstos dos métodos son para que se pueda cargar los items correctamente desde sus archivos .py

def load_item(item_name: str):
    """Método para cargar los items"""
    module_name = f"{ITEM_FOLDER}.{item_name}"
    try:
        module = importlib.import_module(module_name)
        item_class = getattr(module, item_name)
        return item_class()
    except (ModuleNotFoundError, AttributeError):
        raise ImportError(f"No se encontró el item {item_name} en {module_name}")
    
def list_items():
    """Método para listar los items"""
    items = []
    for filename in os.listdir(ITEM_FOLDER):
        if filename.endswith(".py") and filename != "__init__.py":
            items.append(filename[:-3])
    return items


class Item:
    name: str
    cost: int
    sell: int

    hp: int
    hp_regen: float #%
    mana: int
    mana_regen: float #%
    ad: int
    as_: float #%
    ap: int
    armor: int
    mr: int
    healshield_power: float #%
    tenacity: float #%
    crit_chance: float #%
    crit_damage: float #%
    armorpen_flat: int
    armorpen_percent: float #%
    magicpen_flat: int
    magicpen_percent: float #%
    lifesteal: float #%
    ah: int
    movespeed_flat: int
    movespeed_percent: float #%

    def __init__(self, name, cost, sell, hp, hp_regen, mana, mana_regen, ad, as_, ap, armor, mr, healshield_power, tenacity, crit_chance, crit_damage, armorpen_flat, armorpen_percent, magicpen_flat, magicpen_percent, lifesteal, ah, movespeed_flat, movespeed_percent):
        """Constructor"""
        self.name = name
        self.cost = cost
        self.sell = sell
        self.hp = hp
        self.hp_regen = hp_regen
        self.mana = mana
        self.mana_regen = mana_regen
        self.ad = ad
        self.as_ = as_
        self.ap = ap
        self.armor = armor
        self.mr = mr
        self.healshield_power = healshield_power
        self.tenacity = tenacity
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.armorpen_flat = armorpen_flat
        self.armorpen_percent = armorpen_percent
        self.magicpen_flat = magicpen_flat
        self.magicpen_percent = magicpen_percent
        self.lifesteal = lifesteal
        self.ah = ah
        self.movespeed_flat = movespeed_flat
        self.movespeed_percent = movespeed_percent

    def item_info(self):
        """Método para ver las estadisticas que da el item"""
        info = [
            {"icon": None, "value": f"Nombre: {self.name}"},
            {"icon": stat_icon["Gold"], "value": f"Coste: {self.cost}"},
            {"icon": stat_icon["Gold"], "value": f"Vendible por: {self.sell}"}
        ]
        
        stats = {
            "Health": self.hp,
            "Health Regen(%)": (self.hp_regen * 100),
            "Mana": self.mana,
            "Mana Regen(%)": (self.mana_regen * 100),
            "Attack Damage": self.ad,
            "Attack Speed(%)": (self.as_ * 100),
            "Ability Power": self.ap,
            "Armor": self.armor,
            "Magic Resistance": self.mr,
            "Heal & shield power(%)": (self.healshield_power * 100),
            "Tenacity": (self.tenacity * 100),
            "Critical strike chance(%)": (self.crit_chance * 100),
            "Critical strike damage(%)": (self.crit_damage * 100),
            "Lethality": self.armorpen_flat,
            "Armor penetration(%)": (self.armorpen_percent * 100),
            "MagicResist flat penetration": self.magicpen_flat,
            "MagicResist penetration(%)": (self.magicpen_percent * 100),
            "Lifesteal(%)": (self.lifesteal * 100),
            "Ability haste": self.ah,
            "Movement Speed": self.movespeed_flat,
            "Movement Speed(%)": (self.movespeed_percent * 100)
        }
        
        for stat_name, stat_value in stats.items():
            if stat_value > 0:
                icon_path = stat_icon.get(stat_name, None)
                info.append({"icon": icon_path, "value": stat_value})
        return info