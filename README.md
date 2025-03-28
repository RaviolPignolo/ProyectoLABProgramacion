# =-=-=-= Simulador 1v1 entre campones de LoL =-=-=-=
Simula un 1v1 entre los 170 campeones de League of Legends actualizado hasta el parche 25.05

- Nota: Todavía tengo que ver cómo implementar las habilidades de los campeónes, por lo que actualmente el método de ataque solo toma como variables el AD y Armor. Se recomienda el uso de campeones que su daño principal provenga de los Ataques Básicos.
- Nota: Tengo que armar los daños críticos para que funcionen correctamente

## Installation

- Clona el repositorio github
- Instala las dependencias con el comando:
```python
  pip install -r requirements.txt
```
    
## Usage

En el archivo Main.py encontrarás algunos campeones e items ya creados.

```python

 # Comandos de Campeones
    NombreCampeon.level_up()
      # Sube de nivel al campeón, aumentando ciertas estadísticas usando los cálculos de League of Legends
    NombreCampeon.simple_stats()
      # Lista las estadísticas principales del campeón
    NombreCampeon.extended_stats()
      # Lista las demás estadisticas del campeón
    NombreCampeon.as_stats()
      # Lista las estadisticas relacionadas con la velocida de ataque para corroborar el correcto funcionamiento
    NombreCampeon.add_item(NombreItem)
      # Agrega un item al inventario del campeón con un límite de 6
    NombreCampeon.remove_item(NombreItem)
      # Elimina un item del inventario del campeón
    NombreCampeon.item_list()
      # Lista los items que tiene el campeón en el inventario
    NombreCampeon.update_stats()
      # Es utilizado por remove_item y add_item para actualizar las estadisticas de los campeones al darles o quitarles items
    NombreCampeon.realizar_daño(NombreCampeon)
      # El campeón que lo ejecuta iniciará una pelea contra el campeón dado por parámetro hasta que uno de los dos o ambos mueran
    NombreCampeon.recibir_daño(NombreCampeon)
      # El campeón que lo ejecuta calcula el daño que recibe luego de los cálculos
      # (Por ahora solo toma en cuenta el AD y Armor como stats)

      
 # Comandos de items
    NombreItem.item_info()
      # Lista las estadísticas que otorga el item

      
```

## Tests

Para realizar los tests se debe ejecutar el siguiente comando

- Situarse en la ubicación raíz del proyecto y escribir el comando:
```python
  python -m unittest discover -s test
```


## Roadmap

- Agregar todos los campeones (15/170)

- Agregar todos los item
  - Starter: (0/7)
  - Potions and Consumables: (0/6)
  - Basic Items (0/15)
  - Epic Items (0/47)
  - Legendary Items (7/106)

- Implementas habilidades y pasivas de campeones

- Implementar habilidades pasivas y activas de Items

- Pulir el sistema de 1v1

- Implementar entorno gráfico

- Implementar una opción "ver detalles" para ver todos los números cuando se calculan los daños y defensas

## Authors

- [@RaviolPignolo](https://github.com/RaviolPignolo)

