import importlib
import os

EFFECT_FOLDER = "Proyecto.src.Effects"

"""Método para cargar los efectos"""
def load_effect(effect_name: str):
    module_name = f"{EFFECT_FOLDER}.{effect_name}"
    try:
        module = importlib.import_module(module_name)
        effect_class = getattr(module, effect_name)
        return effect_class()
    except (ModuleNotFoundError, AttributeError):
        raise ImportError(f"No se encontró el efecto {effect_name} en {module_name}")

"""Método para listar los efectos"""
def list_effect():
    effects = []
    for filename in os.listdir(EFFECT_FOLDER):
        if filename.endswith(".py") and filename != "__init__.py":
            effects.appends(filename[:-3])
        return effects
    
class Effect:
    name: str
    description: str
    duration: str
    source: str
    type: str
    
    """Constructor"""
    def __init__(self, name, description, duration, source, type):
        self.name = name
        self.description = description
        self.duration = duration
        self.source = source
        self.type = type
        
    """Método para ver la informacion del efecto"""
    def effect_info(self):
        print(f"Nombre: {self.name}")
        print(f"Descripción: {self.description}")
        print(f"Duración: {self.duration}")
        print(f"Origen: {self.source}")
        print(f"Tipo: {self.type}")