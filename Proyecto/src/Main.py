from Champion import Champion
from Item import Item


# Campeones
Karthus = Champion("Karthus", "The Deathsinger", 1, 620, 110, 6.5, 0.55, 467, 31, 8, 0.8, 0, 0, 46, 3.25, 21, 4.7, 30, 1.3, 450, 335, 0.625, 0.625, 0.0211)
Maokai  = Champion("Maokai", "The Twisted Treant", 1, 665, 109, 5, 0.75, 375, 43, 6, 0.6, 0, 0, 64, 3.3, 35, 5.2, 32, 2.05, 125, 335, 0.8, 0.695, 0.02125)
Caitlyn = Champion("Caitlyn", "The Sheriff of Piltover", 1, 580, 107, 3.5, 0.55, 315, 40, 7.4, 0.7, 0, 0, 60, 3.8, 27, 4.7, 30, 1.3, 650, 325, 0.681, 0.625, 0.04)
Twitch = Champion("Twitch", "The Plague Rat", 1, 630, 104, 3.75, 0.6, 300, 40, 7.25, 0.7, 0, 0, 59, 3.1, 27, 4.2, 30, 1.3, 550, 330, 0.679, 0.679, 0.0338)
Jhin = Champion("Jhin", "The Virtuoso", 1, 655, 107, 3.75, 0.55, 300, 50, 6, 0.8, 0, 0, 59, 4.4, 24, 4.7, 30, 1.3, 550, 300, 0.625, 0, 0) # Éste señor Don Especial no obtiene AS como los demás, hay que agregarle una funcion solo para él porque su AS crece de forma linea, no como los demas
TahmKench = Champion("Tahm Kench", "The River King", 1, 640, 103, 6.5, 0.55, 325, 50, 8, 1, 0, 0, 56, 3.2, 39, 4.7, 32, 2.05, 175, 335, 0.658, 0.658, 0.025)
Nautilus = Champion("Nautilus", "The Titan of the depths", 1, 646, 100, 8.5, 0.55, 400, 47, 8.65, 0.5, 0, 0, 61, 3.3, 39, 4.95, 32, 2.05, 175, 325, 0.706, 0.612, 0.01)

# Items
Guinsoo = Item("Guinsoo's Rageblade", 3000, 2100, 0, 0, 0, 0, 30, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Opportunity = Item("Opportunity", 2700, 1890, 0, 0, 0, 0, 55, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0 , 0, 0, 0)
Bloodthirster = Item("Bloodthirster", 3400, 2380, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0, 0, 0)
#Revisar SpiritVisage que se aplique correctamente el 100% de regeneración de vida
SpiritVisage = Item("Spirit Visage", 2700, 1890, 400, 1.00, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0)
Thornmail = Item("Thornmail", 2450, 1715, 150, 0, 0, 0, 0, 0, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Jaksho = Item("Jak'sho, The Protean", 3200, 2240, 350, 0, 0, 0, 0, 0, 0, 45, 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

Twitch.realizar_daño(Maokai)