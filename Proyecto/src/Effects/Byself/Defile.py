from Proyecto.src import Effect

class Defile(Effect):
    def __init__(self):
        super().__init__(
            name = "Defile"
            description = "Karthus is draining his Mana to damage nearby enemies each second"
            duration = " "
            source = "Karthus"
            type = "Debuff"
        )