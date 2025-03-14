# =-=-=-= Simulador 1v1 entre campones de LoL =-=-=-=
Simula un 1v1 entre los 170 campeones de League of Legends actualizado hasta el parche 25.05

- Version 0.1

- Notas: Todavía tengo que ver cómo implementar las habilidades de los campeónes, por lo que actualmente solo se podrán hacer daño mediante Ataques Básicos. Se recomienda el uso de campeones que su daño principal provenga de los Ataques Básicos.
                               
## Installation

. Clona el repositorio github
. Instala las dependencias

```python
  pip install -r requirements.txt
```
    
## Usage

En el archivo Main.py encontrarás algunos campeones e items ya creados.

Por ahora solo se pueden ver las estadisticas de los campeones e items y agregarle items a los campeones (aunque no le suma estadisticas al campeón (Aún) )

```python

 # Comandos de Campeones
    NombreCampeon.level_up()
      # Sube de nivel al campeón, aumentando ciertas estadísticas usando los cálculos de League of Legends
    NombreCampeon.simple_stats()
      # Lista las estadísticas principales del campeón
    NombreCampeon.extended_stats()
      # Lista las demás estadisticas del campeón
    NombreCampeon.add_item(NombreItem)
      # Agrega un item al inventario del campeón con un límite de 6
    NombreCampeon.remove_item(NombreItem)
      # Elimina un item del inventario del campeón
    NombreCampeon.item_list()
      # Lista los items que tiene el campeón en el inventario

 # Comandos de items
    NombreItem.item_info()
      # Lista las estadísticas que otorga el item

      
```


## Roadmap

- Agregar todos los campeones (7/170)

- Agregar todos los item
  - Starter: (0/7)
  - Potions and Consumables: (0/6)
  - Basic Items (0/15)
  - Epic Items (0/47)
  - Legendary Items (6/106)

- Implementas habilidades y pasivas de campeones

- Implementar habilidades pasivas y activas de Items

- Pulir el sistema de 1v1

- Implementar entorno gráfico

- Implementar una opción "ver detalles" para ver todos los números cuando se calculan los daños y defensas
## Authors

- [@RaviolPignolo](https://github.com/RaviolPignolo)

