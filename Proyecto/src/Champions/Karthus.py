from ..Champion import Champion

class Karthus(Champion):
    def __init__(self):
        super().__init__(
            name = "Karthus",
            title = "The Deathsinger",
            level = 1,
            base_hp = 620,
            base_hp_g = 110,
            base_hp_regen= 6.5, 
            base_hp_regen_g = 0.55,
            base_mana = 467,
            base_mana_g = 31,
            base_mana_regen = 8,
            base_mana_regen_g = 0.8,
            base_energy = 0,
            base_energy_g = 0, 
            base_ad = 46,
            base_ad_g = 3.25,
            base_armor = 21,
            base_armor_g = 4.7,
            base_mr = 30,
            base_mr_g = 1.3,
            base_range = 450,
            base_move_speed = 335,
            base_as = 0.625,
            as_ratio = 0.625,
            bonus_as = 0.0211,
        )
        
    
    """
    [P] Death Defied
    Upon taking faltal damage, Karthus enters a zombie state for 7 seconds, during which he can cast abilities at no cost.
    If Defile(E) has been learned, it will remain toggled on for Death Defiles's duration.
    Requiem(R) becomes disabled after Death Defied has lasted 4 seconds.
    
    While under this state, Karthus becomes untergetable and immune to crowd control as well as prevents all incomings damage,
    but is also rendered unable to move, declare basic attacks, use summoner spells, and activate items.
    """
    def pasiva(self):
        super().pasiva()
        
    """
    [Q] Lay Waste    1s    20 Mana
    Karthus creates a blast of magic, dealing x=(40 +35%AP) magic damage.
    If the blast hits only one enemy, it instead deal x=(80 +70%AP) magic damage.
    
    Damage          [40/59/78/97/116]
    Mana Cost       [20/25/30/35/40]
    """
    def q(self): #Hasta implementar el sistema de subir de niveles las habildiades hasta 5 el daño será siempre como si fuesen de nivel 1
        # La terminal indica el uso de la habilidad
        super().q()
        #Códigod de la habilidad
        damage = 80 + (0.7 * self.actual_ap) #Uso el daño potenciado porque al ser 1v1 siempre va a ser una Q aislada
        #Dar los resultados
        return damage
        
    """
    [W] Wall of Pain    15s    70 Mana
    Karthus creates a wall that lasts for 5 seconds.
    Enemies that pass through lose 25% Magic Resist for 5 seconds and are Slowed by 40% decaying over the duration.
    
    Wall Width          [800/900/1000/1100/1200]
    Move Speed Slow     [40%/50%/60%/70%/80%]
    """
    def w(self):
        super().w()

    """
    [E] Defile    0.5s    30 Mana per Second
    Passive: When Karthus kills a unit, he restores 10 Mana.
    Toggle: Karthus creates a necrotic aura, dealing x=(30 +20%AP) magic damage per second to nearby enemies.
    
    Damage per Second   [30/50/70/90/110]
    Mana Restore        [10/20/30/40/50]
    Mana Cost           [30/42/54/66/78]
    """
    def e(self):
        super().e()
        damage = 30+(0.2*self.actual_ap)
        return damage
    """
    [R] Requiem    188.68s    100 Mana
    Karthus channels for 3 seconds, then deals x=(200 +70%AP) magic damage to enemy champions, regardless of distance.
    
    Damage      [200/350/500]
    Cooldown    [188.68/169.81/150.94]
    """    
    def r(self):
        super().r()
        damage = 200+(0.7 * self.actual_ap)
        return damage