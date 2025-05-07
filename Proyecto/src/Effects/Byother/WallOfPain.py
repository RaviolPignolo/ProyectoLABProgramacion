from Proyecto.src import Effect

class WallOfPainMR_Debuff(Effect):
    def __init__(self):
        super().__init__(
            name = "Wall of Pain"
            description = "This unit's Magic Resist is reduced\n This unit's Move Speed has been greatly reduced and it is slowly returning to normal"
            duration = " " #15
            source = "Karthus"
            type = "Debuff"
        )
        
        #Cuando Karthus usa R a los enemigos les sale:
        # Requiem
        # This unit is about to take damage
        # Karthus