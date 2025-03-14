
        #### Abilidades Pasivas WIP ####

class Item:

    name: str
    cost: int
    sell: int

    # Stats que pueden dar los items
    health: int
    healthRegen: float #%
    mana: int
    manaRegen: float #%
    attackDamage: int
    attackSpeed: float #%
    abilityPower: int
    armor: int
    magicResist: int
    healShieldPower: float #%
    tenacity: float #%
    criticalStrikeChance: float #%
    criticalStrikeDamage: float #%
    armorPenetrationFlat: int
    armorPenetrationPercent: float #%
    magicPenetrationFlat: int
    magicPenetrationPercent: float #%
    lifeSteal: float #%
    abilityHaste: int
    moveSpeedFlat: int
    moveSpeed: float #%

    #Los dejo como estadistica del item o habilidad? o.o?
    # healReduction
    # shieldReduction
    #omnivamp

    # Constructor
    def __init__(self, name, cost, sell, health, healthRegen, mana, manaRegen, attackDamage, attackSpeed, abilityPower, armor, magicResist, healShieldPower, tenacity, criticalStrikeChance, criticalStrikeDamage, armorPenetrationFlat, armorPenetrationPercent, magicPenetrationFlat, magicPenetrationPercent, lifeSteal, abilityHaste, moveSpeedFlat, moveSpeed):
        self.name = name
        self.cost = cost
        self.sell = sell
        self.health = health
        self.healthRegen = healthRegen
        self.mana = mana
        self.manaRegen = manaRegen
        self.attackDamage = attackDamage
        self.attackSpeed = attackSpeed
        self.abilityPower = abilityPower
        self.armor = armor
        self.magicResist = magicResist
        self.healShieldPower = healShieldPower
        self.tenacity = tenacity
        self.criticalStrikeChance = criticalStrikeChance
        self.criticalStrikeDamage = criticalStrikeDamage
        self.armorPenetrationFlat = armorPenetrationFlat
        self.armorPenetrationPercent = armorPenetrationPercent
        self.magicPenetrationFlat = magicPenetrationFlat
        self.magicPenetrationPercent = magicPenetrationPercent
        self.lifeSteal = lifeSteal
        self.abilityHaste = abilityHaste
        self.moveSpeedFlat = moveSpeedFlat
        self.moveSpeed = moveSpeed

    
    def item_info(self):
        print("Nombre: ", self.name)
        print("Coste: ", self.cost, " Oro")
        print("Vendible por: ", self.sell, " Oro")
        
        stats = {
        #   stat_name: stat_value
            "Health": self.health,
            "Health Regen(%)": (self.healthRegen * 100),
            "Mana": self.mana,
            "Mana Regen(%)": (self.manaRegen * 100),
            "Attack Damage": self.attackDamage,
            "Attack Speed(%)": (self.attackSpeed * 100),
            "Ability Power": self.abilityPower,
            "Armor": self.armor,
            "Magic Resistance": self.magicResist,
            "Heal & shield power(%)": (self.healShieldPower * 100),
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
        # Mostrar solo estadisticas que sean mayores a 0
        for stat_name, stat_value in stats.items():
            if stat_value > 0:
                print(f"{stat_name}: {stat_value}")