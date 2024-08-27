# Desafío - Tipos de Métodos - Juego Gran Fantasía

 En este desafío se validan conocimientos de codificación de clases con métodos
 constructores, accesadores, mutadores y sobrecarga.


## Descripción

 Se ha solicitado desarrollar el algoritmo de la primera escena del juego “Gran Fantasía”
 

## El juego 

Bienvenido a "Gran Fantasía", un juego de consola de texto donde te enfrentarás a un orco en un combate por la experiencia y la victoria.


## Cómo Jugar

1. **Clona el repositorio:** 
   
   ```bash
   git clone https://github.com/bhahumada/tipos_de_metodos_juego_gran_fantasia.git 
   ```

2. **Navega a la carpeta del juego:**

  cd gran-fantasia

3. **Ejecuta el juego:**
   python juego.py

4. **Reglas del Juego**

Se te pedirá que ingreses el nombre de tu personaje.
Tu personaje comienza en el nivel 1 con 0 puntos de experiencia.
En cada turno, te enfrentarás a un orco.
Puedes elegir entre Atacar o Huir.

La probabilidad de ganar depende de tu nivel en comparación con el del orco:
Mayor nivel: 66% de probabilidad de ganar.
Igual nivel: 50% de probabilidad de ganar.
Menor nivel: 33% de probabilidad de ganar.

Si ganas un combate, ganarás experiencia. Si pierdes, perderás experiencia (a menos que ya tengas 0).
Cada 100 puntos de experiencia, subirás de nivel.
El juego termina cuando decides huir o cierras la consola.


## Archivos

juego.py: Contiene la lógica principal del juego y la función main.
personaje.py: Define la clase Personaje con sus atributos y métodos.


## Requisitos

Python 3.6 o superior


## Autor

Bárbara HA.

Github: https://github.com/bhahumada/tipos_de_metodos_juego_gran_fantasia.git 