import unittest
from src.Champion import load_champion #Importo el metodo para cargar los campeones
from src.Item import load_item #Importo el metodo para cargar los items
from src.Champion import Champion # Importo la clase Champion
# Importo los campeones de su propio archivo .py
from src.Champions import Karthus
from src.Champions import Twitch 
from src.Champions import Maokai 
from src.Champions import Aatrox 
from src.Item import Item # Importo la clase Item
# Importo los items de su propio archivo .py
from src.Items import Guinsoo
from src.Items import Opportunity
from src.Items import BlackfireTorch
from src.Items import Thornmail
from src.Items import SpiritVisage


class TestChampion(unittest.TestCase):
    def set_up(self): 
        Karthus.load_champion("Karthus") # Un mago
        Twitch.load_champion("Twitch")   # Un tirador
        Maokai.load_champion("Maokai")   # Un tanque
        Aatrox.load_champion("Aatrox")   # Un luchador

        Guinsoo.load_item("Guinsoo")     # Un item con ad, ap y as
        Opportunity.load_item("Opportunity") # Un item con ad y penetracion plana de armadura
        BlackfireTorch.load_item("BlackfireTorch") # Un item con ap, mana y ah
        Thornmail.load_item("Thornmain") # Un item de armadura
        SpiritVisage.load_item("SpiritVisage") # Un item de resistencia magica
    

    def test_carga_instancia(self):
        """Verifica que los campeones e items se creen correctamente"""
        champ = load_champion("Karthus")
        item = load_item("BlackfireTorch")
        self.assertIsInstance(champ, Champion)
        self.assertIsInstance(item, Item)


    def test_level_up(self):
        """Verifica que al subir de nivel aumenten correctamente las estadisticas"""
        Karthus_hp_inicial = self.Karthus.actual_hp
        Karthus_hp_regen_inicial = self.Karthus.hp_regen
        Karthus_mana_inicial = self.Karthus.actual_mana
        Karthus_mana_regen_inicial = self.Karthus.mana_regen
        Karthus_ad_inicial = self.Karthus.actual_ad
        Karthus_as_inicial = self.Karthus.actual_as
        Karthus_armor_inicial = self.Karthus.actual_armor
        Karthus_mr_inicial = self.Karthus.actual_mr

        self.Karthus.level_up()

        self.assertGreater(self.Karthus.actual_hp, Karthus_hp_inicial)
        self.assertGreater(self.Karthus.hp_regen, Karthus_hp_regen_inicial)
        self.assertGreater(self.Karthus.actual_mana, Karthus_mana_inicial)
        self.assertGreater(self.Karthus.mana_regen, Karthus_mana_regen_inicial)
        self.assertGreater(self.Karthus.actual_ad, Karthus_ad_inicial)
        self.assertGreater(self.Karthus.actual_as, Karthus_as_inicial)
        self.assertGreater(self.Karthus.actual_armor, Karthus_armor_inicial)
        self.assertGreater(self.Karthus.actual_mr, Karthus_mr_inicial)

    def test_add_item(self):
        """Verifica que al agregar items aumenten las estadisticas correctamente de forma acumulativa"""
        #Stats de Guinsoo (ad, ap, as)
        Karthus_ad_inicial = self.Karthus.actual_ad
        Karthus_ap_inicial = self.Karthus.actual_ap
        Karthus_as_inicial = self.Karthus.actual_as

        self.Karthus.add_item(self.Guinsoo)

        self.assertGreater(self.Karthus.actual_ad, Karthus_ad_inicial)
        self.assertGreater(self.Karthus.actual_ap, Karthus_ap_inicial)
        self.assertGreater(self.Karthus.actual_as, Karthus_as_inicial)
        #Stats de Opportunity (ad, armorpen_flat)
        Karthus_ad_inicial_2 = self.Karthus.actual_ad
        Karthus_armorpen_flat_inicial = self.Karthus.armorpen_flat
        
        self.Karthus.add_item(self.Opportunity)

        self.assertGreater(self.Karthus.actual_ad, Karthus_ad_inicial_2)
        self.assertGreater(self.Karthus.armorpen_flat, Karthus_armorpen_flat_inicial)
        #Stats de BlackfireTorch (ap, mana, ah)
        Karthus_ap_inicial_2 = self.Karthus.actual_ap
        Karthus_mana_inicial = self.Karthus.actual_mana
        Karthus_ah_inicial = self.Karthus.actual_ah

        self.Karthus.add_item(self.BlackfireTorch)

        self.assertGreater(self.Karthus.actual_ap, Karthus_ap_inicial_2)
        self.assertGreater(self.Karthus.actual_mana, Karthus_mana_inicial)
        self.assertGreater(self.Karthus.actual_ah, Karthus_ah_inicial)
        #Stats de Thornmain (hp, armor)
        Karthus_hp_inicial = self.Karthus.actual_hp
        Karthus_armor_inicial = self.Karthus.actual_armor

        self.Karthus.add_item(self.Thornmain)

        self.assertGreater(self.Karthus.actual_hp, Karthus_hp_inicial)
        self.assertGreater(self.Karthus.actual_armor, Karthus_armor_inicial)
        #Stats de SpiritVisage (ah, hp, hp_regen, mr)
        Karthus_ah_inicial_2 = self.Karthus.actual_ah
        Karthus_hp_inicial_2 = self.Karthus.actual_hp
        Karthus_hp_regen_inicial = self.Karthus.hp_regen
        Karthus_mr_inicial = self.Karthus.actual_mr

        self.Karthus.add_item(self.SpiritVisage)

        self.assertGreater(self.Karthus.actual_ah, Karthus_ah_inicial_2)
        self.assertGreater(self.Karthus.actual_hp, Karthus_hp_inicial_2)
        self.assertGreater(self.Karthus.hp_regen, Karthus_hp_regen_inicial)
        self.assertGreater(self.Karthus.actual_mr, Karthus_mr_inicial)

    def test_remove_item(self):
        """Verifica que al remover items se disminuyan las estadisticas correspondientes de forma sustractiva"""
        self.Karthus.add_item(self.Thornmail)
        self.Karthus.add_item(self.SpiritVisage)

        Karthus_hp_inicial = self.Karthus.actual_hp
        Karthus_hp_regen_inicial = self.Karthus.hp_regen
        Karthus_armor_inicial = self.Karthus.actual_armor
        Karthus_mr_inicial = self.Karthus.actual_mr
        Karthus_ah_inicial = self.Karthus.actual_ah

        self.Karthus.remove_item(self.Thornmail)

        self.assertLess(self.Karthus.actual_hp, Karthus_hp_inicial)
        self.assertLess(self.Karthus.actual_armor, Karthus_armor_inicial)

        self.Karthus.remove_item(self.SpiritVisage)

        self.assertLess(self.Karthus.actual_hp, Karthus_hp_inicial)
        self.assertLess(self.Karthus.hp_regen, Karthus_hp_regen_inicial)
        self.assertLess(self.Karthus.actual_ah, Karthus_ah_inicial)
        self.assertLess(self.Karthus.actual_mr, Karthus_mr_inicial)

    def test_list_items(self):
        """Verifiacar que se listen los items correctamente cuando se le dan más item del máximo de inventario (6)"""
        self.Karthus.add_item(self.Guinsoo)
        self.Karthus.add_item(self.Opportunity)
        self.Karthus.add_item(self.BlackfireTorch)
        self.Karthus.add_item(self.Thornmain)
        self.Karthus.add_item(self.SpiritVisage)
        self.Karthus.add_item(self.BlackfireTorch) # último slot de inventario
        self.Karthus.add_item(self.BlackfireTorch) # no se debería agregar
        self.Karthus.add_item(self.BlackfireTorch) # no se debería agregar

        self.assertEqual(self.Karthus.list_items(), ["Guinsoo", "Opportunity", "BlackfireTorch", "Thornmain", "SpiritVisage", "BlackfireTorch"])

    def test_realizar_daño_sinitems(self, enemy):
        """Verficamos que los campeones se ataquen correctamente"""
        Twitch_hp_inicial = self.Twitch.actual_hp
        Aatrox_hp_inicial = self.Aatrox.actual_hp

        self.Twitch.realizar_daño(self.Aatrox)

        # Verifica que los dos reciban daño
        self.assertLess(self.Aatrox.actual_hp, Aatrox_hp_inicial)
        self.assertLess(self.Twitch.actual_hp, Twitch_hp_inicial)

        # Verifica si Twitch murio y Aatrox sigue vivo
        if (self.Twitch.actual_hp <= 0):
            self.assertEqual(self.Twitch.actual_hp, 0)
            self.assertFalse(self.Twitch.its_alive)
        if (self.Aatrox.its_alive):
            self.assertGreater(self.Aatrox.actual_hp, 0)

        # Verifica si Aatrox murio y Twitch sigue vivo
        if (self.Aatrox.actual_hp <= 0):
            self.assertEqual(self.Aatrox.actual_hp, 0)
            self.assertFalse(self.Aatrox.its_alive)
        if (self.Twitch.its_alive):
            self.assertGreater(self.Twitch.actual_hp, 0)

        # Verifica si ambos murieron
        if not (self.Aatrox.its_alive) and not (self.Twitch.its_alive):
            self.assertEqual(self.Aatrox.actual_hp, 0)
            self.assertEqual(self.Twitch.actual_hp, 0)
        

    def test_realizar_daño_conitems(self, enemy):
        """Verficamos que los campeones se ataquen correctamente con items"""
        Twitch_hp_inicial = self.Twitch.actual_hp
        Maokai_hp_inicial = self.Maokai.actual_hp

        self.Twitch.add_item(self.Oppotunity)
        self.Maokai.add_item(self.Thornmain)

        self.Twitch.realizar_daño(self.Maokai)

        # Verifica que los dos reciban daño
        self.assertLess(self.Maokai.actual_hp, Maokai_hp_inicial)
        self.assertLess(self.Twitch.actual_hp, Twitch_hp_inicial)

        # Verifica si Twitch murio y Maokai sigue vivo
        if (self.Twitch.actual_hp <= 0):
            self.assertEqual(self.Twitch.actual_hp, 0)
            self.assertFalse(self.Twitch.its_alive)
        if (self.Maokai.its_alive):
            self.assertGreater(self.Maokai.actual_hp, 0)

        # Verifica si Maokai murio y Twitch sigue vivo
        if (self.Maokai.actual_hp <= 0):
            self.assertEqual(self.Maokai.actual_hp, 0)
            self.assertFalse(self.Maokai.its_alive)
        if (self.Twitch.its_alive):
            self.assertGreater(self.Twitch.actual_hp, 0)

        # Verifica si ambos murieron
        if not (self.Maokai.its_alive) and not (self.Twitch.its_alive):
            self.assertEqual(self.Maokai.actual_hp, 0)
            self.assertEqual(self.Twitch.actual_hp, 0)

    
    def test_muerte_instantanea(self):
        """Verifica que un campeón muera al recibir suficiente daño de un golpe"""
        Aatrox.actual_ad = 1000
        self.Aatrox.realizar_daño(self.Maokai)
        self.assertFalse(self.Maokai.its_alive)
        self.assertEqual(self.Maokai.actual_hp, 0)