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
    
    q_level = 1
    w_level = 1
    e_level = 1
    r_level = 1
    
    p_name = " "
    q_name = " "
    w_name = " "
    e_name = " "
    r_name = " "
    
    e_toggle = False
    
    def level_up_hability(self, hability):
        super().level_up_hability(hability)
    
    """
    [P] Death Defied
    Upon taking faltal damage, Karthus enters a zombie state for 7 seconds, during which he can cast abilities at no cost.
    If Defile(E) has been learned, it will remain toggled on for Death Defiles's duration.
    Requiem(R) becomes disabled after Death Defied has lasted 4 seconds.
    
    While under this state, Karthus becomes untergetable and immune to crowd control as well as prevents all incomings damage,
    but is also rendered unable to move, declare basic attacks, use summoner spells, and activate items.
    """
    # Hacer en Champion.py que cuando un campeon muere se llama a una funcion que setea its_live a False,
    # asi Karthus, KogMaw y Sion reescriben ese metodo para que al morir se active la pasiva de tipo zombie
    # y luego se muere el champ por completo y setea por completo its_live a False
    
    def pasiva(self):
        super().pasiva()
        
    """
    [Q] Lay Waste    1s    20 Mana
    Karthus creates a blast of magic granting sight and dealing x=(40 +35%AP) magic damage.
    If the blast hits only one enemy, it instead deal x=(80 +70%AP) magic damage.
    During Death Defied, Lay Waste will cast at maximum range if cast beyond that.
    
    Damage          [40/59/78/97/116]
    Enhanced Damage [80/118/156/194/232]
    Mana Cost       [20/25/30/35/40]
    """
    def q(self, Champion):
        mana_cost = 0
        damage = 0
        tipo = "AP"
    
        if(self.q_level == 1):
            mana_cost = 20
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear Q")
            else:
                super().q()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)
                damage = 80 + (0.7 * self.actual_ap) #Uso el daño potenciado porque al ser 1v1 siempre va a ser una Q aislada
                super().hacer_daño(damage, tipo, Champion)
                
        if(self.q_level == 2):
            mana_cost = 25
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear Q")
            else:
                super().q()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)
                damage = 118 + (0.7 * self.actual_ap)
                super().hacer_daño(damage, tipo, Champion)
        
        if(self.q_level == 3):
            mana_cost = 30
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear Q")
            else:
                super().q()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)
                damage = 156 + (0.7 * self.actual_ap)
                super().hacer_daño(damage, tipo, Champion)
                
        if(self.q_level == 4):
            mana_cost = 35
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear Q")
            else:
                super().q()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)
                damage = 194 + (0.7 * self.actual_ap)
                super().hacer_daño(damage, tipo, Champion)
                
        if(self.q_level == 5):
            mana_cost = 40
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear Q")
            else:
                super().q()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)
                damage = 232 + (0.7 * self.actual_ap)
                super().hacer_daño(damage, tipo, Champion)
        
            
        
    """
    [W] Wall of Pain    Cost: 70 Mana    Cooldown: 15s
    Active: Karthus raise a wall of pain at the target location perpendicular to his facing that lasts 5s, granting sight around its pillars and center.
    Enemies that touch the wall are inflicted with 25% magic resistance reduction and become slowed for 5 seconds, decaying over the duration.
    This can affect enemies only once per cast
    
    Wall Lenght          [800/900/1000/1100/1200]
    Move Speed Slow     [40%/50%/60%/70%/80%]
    """
    def w(self, Champion):
        mana_cost = 70
                
        if(self.w_level == 1):
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear W.")
            else:
                super().w()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)

                # Aplicar lógica de reducción de movimiento

                if(Champion.actual_total_mr <= 0):
                    print(f"El MR de {Champion.name} es 0 o menos y no se puede reducir más.")
                else:
                    Champion.actual_total_mr = (Champion.actual_total_mr * (1 - 0.25))
                    
        if(self.w_level == 2):
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear W.")
            else:
                super().w()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)

                # Aplicar lógica de reducción de movimiento

                if(Champion.actual_total_mr <= 0):
                    print(f"El MR de {Champion.name} es 0 o menos y no se puede reducir más.")
                else:
                    Champion.actual_total_mr = (Champion.actual_total_mr * (1 - 0.25))
        
        if(self.w_level == 3):
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear W.")
            else:
                super().w()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)

                # Aplicar lógica de reducción de movimiento

                if(Champion.actual_total_mr <= 0):
                    print(f"El MR de {Champion.name} es 0 o menos y no se puede reducir más.")
                else:
                    Champion.actual_total_mr = (Champion.actual_total_mr * (1 - 0.25))
                    
        if(self.w_level == 4):
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear W.")
            else:
                super().w()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)

                # Aplicar lógica de reducción de movimiento

                if(Champion.actual_total_mr <= 0):
                    print(f"El MR de {Champion.name} es 0 o menos y no se puede reducir más.")
                else:
                    Champion.actual_total_mr = (Champion.actual_total_mr * (1 - 0.25))
                    
        if(self.w_level == 5):
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear W.")
            else:
                super().w()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)

                # Aplicar lógica de reducción de movimiento

                if(Champion.actual_total_mr <= 0):
                    print(f"El MR de {Champion.name} es 0 o menos y no se puede reducir más.")
                else:
                    Champion.actual_total_mr = (Champion.actual_total_mr * (1 - 0.25))
        


    """
    [E] Defile    0.5s    30 Mana per Second
    Passive: When Karthus kills a unit, he restores 10 Mana.
    Toggle: Karthus surrounds himself with a necrotic aura that deals x=(7.5 +5%AP) every 0.25s(tick) (equal to x=(30 +20%AP) every 1s) to all nearby enemies.
    Toggling Defile off triggers a final tick of damage.
    Defile cannot be toggled off during Death Defied
    
    Damage per Tick     [7.5/12.5/17.5/22.5/27.5]
    Damage per Second   [30/50/70/90/110]
    Mana Restore        [10/20/30/40/50]   Ver cómo aplicarlo
    Mana Cost           [30/42/54/66/78]
    """
    def e(self, Champion):
        mana_cost = 0
        damage = 0
        tipo = "AP"

        if(self.e_toggle == True):
            print(f"{self.name} desactiva E")
            damage = 7.5 + (0.05 * self.actual_ap)
            super().hacer_daño(damage, tipo, Champion)
            self.e_toggle = False
        else:
            if(self.e_level == 1):
                mana_cost = 30
                if(self.actual_mana < mana_cost):
                    print(f"{self.name} no tiene suficiente maná para castear E")
                else:
                    super().e()
                    self.e_toggle = True
                    self.actual_mana = max(self.actual_mana - mana_cost, 0)
                    damage = (7.5 + (0.05 * self.actual_ap)) * 4 # La idea es obtener el daño x segundo y cuando se desactive activar el ultimo tick
                    super().hacer_daño(damage, tipo, Champion)
            
            if(self.e_level == 2):
                mana_cost = 42
                if(self.actual_mana < mana_cost):
                    print(f"{self.name} no tiene suficiente maná para castear E")
                else:
                    super().e()
                    self.e_toggle = True
                    self.actual_mana = max(self.actual_mana - mana_cost, 0)
                    damage = (12.5 + (0.05 * self.actual_ap)) * 4
                    super().hacer_daño(damage, tipo, Champion)
                    
            if(self.e_level == 3):
                mana_cost = 54
                if(self.actual_mana < mana_cost):
                    print(f"{self.name} no tiene suficiente maná para castear E")
                else:
                    super().e()
                    self.e_toggle = True
                    self.actual_mana = max(self.actual_mana - mana_cost, 0)
                    damage = (17.5 + (0.05 * self.actual_ap)) * 4
                    super().hacer_daño(damage, tipo, Champion)
                    
            if(self.e_level == 4):
                mana_cost = 66
                if(self.actual_mana < mana_cost):
                    print(f"{self.name} no tiene suficiente maná para castear E")
                else:
                    super().e()
                    self.e_toggle = True
                    self.actual_mana = max(self.actual_mana - mana_cost, 0)
                    damage = (22.5 + (0.05 * self.actual_ap)) * 4
                    super().hacer_daño(damage, tipo, Champion)
                    
            if(self.e_level == 5):
                mana_cost = 78
                if(self.actual_mana < mana_cost):
                    print(f"{self.name} no tiene suficiente maná para castear E")
                else:
                    super().e()
                    self.e_toggle = True
                    self.actual_mana = max(self.actual_mana - mana_cost, 0)
                    damage = (27.5 + (0.05 * self.actual_ap)) * 4
                    super().hacer_daño(damage, tipo, Champion)
                
    
    
    
    """
    [R] Requiem    200s    100 Mana
    Karthus channels for 3 seconds, then deals x=(200 +70%AP) magic damage to enemy champions, regardless of distance.
    
    Damage      [200/350/500]
    Cooldown    [200/180/160] (Starts on-cast)
    """    
    def r(self, Champion):
        mana_cost = 100
        damage = 0
        tipo= "AP"
        
        if(self.r_level == 1):
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear R")
            else:
                super().r()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)
                damage = 200 + (0.7 * self.actual_ap)
                super().hacer_daño(damage, tipo, Champion)
                
        elif(self.r_level == 2):
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear R")
            else:
                super().r()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)
                damage = 350 + (0.7 * self.actual_ap)
                super().hacer_Daño(damage, tipo, Champion)
                
        elif(self.r_level == 3):
            if(self.actual_mana < mana_cost):
                print(f"{self.name} no tiene suficiente maná para castear R")
            else:
                super().r()
                self.actual_mana = max(self.actual_mana - mana_cost, 0)
                damage = 500 + (0.7 * self.actual_ap)
                super().hacer_Daño(damage, tipo, Champion)
            