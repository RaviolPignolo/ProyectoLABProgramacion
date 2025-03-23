import importlib
import os

ITEMS_FORLDER = "Items" # Carpeta que contiene los items

# Éstos dos métodos son para que el Main pueda cargar los items correctamente desde sus archivos .py

# Método para cargar los items
def load_item(item_name: str):
    module_name = f"{ITEMS_FORLDER}.{item_name}"
    try:
        module = importlib.import_module(module_name)
        item_class = getattr(module, item_name)
        return item_class()
    except (ModuleNotFoundError, AttributeError):
        raise ImportError(f"No se encontró el item {item_name} en {module_name}")
    
# Método para listar los items
def list_items():
    items = []
    for filename in os.listdir(ITEMS_FORLDER):
        if filename.endswith(".py") and filename != "__init__.py":
            items.append(filename[:-3])
    return items


class Item:
    name: str
    cost: int
    sell: int

    # Stats que pueden dar los items
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


    # Constructor
    def __init__(self, name, cost, sell, hp, hp_regen, mana, mana_regen, ad, as_, ap, armor, mr, healshield_power, tenacity, crit_chance, crit_damage, armorpen_flat, armorpen_percent, magicpen_flat, magicpen_percent, lifesteal, ah, movespeed_flat, movespeed_percent):
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

    # Método para ver las estadisticas que da el item
    def item_info(self):
        print("Nombre: ", self.name)
        print("Coste: ", self.cost, " Oro")
        print("Vendible por: ", self.sell, " Oro")
        
        stats = {       # Creo un diccionario creando el nombre de la estadistica y asignandole un valor
        #   stat_name: stat_value
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
            "Critical strike chance(%)": (self.criticalStrikeChance * 100),
            "Critical strike damage(%)": (self.criticalStrikeDamage * 100),
            "Lethality": self.armorPenetrationFlat,
            "Armor penetration(%)": (self.armorPenetrationPercent * 100),
            "MagicResist flat penetration": self.magicPenetrationFlat,
            "MagicResist penetration(%)": (self.magicPenetrationPercent * 100),
            "Lifesteal(%)": (self.lifeSteal * 100),
            "Ability haste": self.abilityHaste,
            "Movement Speed": self.moveSpeedFlat,
            "Movement Speed(%)": (self.moveSpeed * 100)
        }
        # Recorro el diccionario y muestro los valores mayores a 0 que tenga el item
        for stat_name, stat_value in stats.items():
            if stat_value > 0:
                print(f"{stat_name}: {stat_value}")