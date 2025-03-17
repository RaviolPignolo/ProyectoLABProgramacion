from Champion import Champion
from Champion import load_champion
from Item import Item

# Campeones
Aatrox = load_champion("Aatrox")
Ahri = load_champion("Ahri")
Akali = load_champion("Akali")
Akshan = load_champion("Akshan")
Alistar = load_champion("Alistar")
Ambessa = load_champion("Ambessa")
Amumu = load_champion("Amumu")
Anivia = load_champion("Anivia")
Caitlyn = load_champion("Caitlyn")
Jhin = load_champion("Jhin")
Karthus = load_champion("Karthus")
Maokai = load_champion("Maokai")
Nautilus = load_champion("Nautilus")
TahmKench = load_champion("TahmKench")
Twitch = load_champion("Twitch")

# Items
Guinsoo = Item("Guinsoo's Rageblade", 3000, 2100, 0, 0, 0, 0, 30, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Opportunity = Item("Opportunity", 2700, 1890, 0, 0, 0, 0, 55, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0 , 0, 0, 0)
Bloodthirster = Item("Bloodthirster", 3400, 2380, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0, 0, 0)
#Revisar SpiritVisage que se aplique correctamente el 100% de regeneración de vida
SpiritVisage = Item("Spirit Visage", 2700, 1890, 400, 1.00, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0)
Thornmail = Item("Thornmail", 2450, 1715, 150, 0, 0, 0, 0, 0, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Jaksho = Item("Jak'sho, The Protean", 3200, 2240, 350, 0, 0, 0, 0, 0, 0, 45, 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

Twitch.simple_stats()