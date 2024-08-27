"""Juego de consola Gran Fantasía."""
from personaje import Personaje
from random import uniform

def main():
    """Función principal del juego.
    Bienvenida y creaci´´on de un personaje,
    Opciones del juego,
    Probabilidad de ganar,
    Asignación de puntajes de experiencia y
    mensajes de estado"""

    print("\n¡Bienvenido a Gran Fantasía!")
    nombre_jugador = input("\nPor favor indique nombre de su personaje: ")

    jugador = Personaje(nombre_jugador)
    orco = Personaje("Orco")

    print(jugador.obtener_estado())

    jugando = True
    while jugando:
        # Cálculo probabilidad de ganar en cada turno
        probabilidad_victoria = jugador.probabilidad_ganar(orco)  

        opcion = jugador.dialogo_enfrentamiento(probabilidad_victoria, orco)

        if opcion == 1:  # Atacar
            if uniform(0, 1) <= probabilidad_victoria:
                print("\n¡Le has ganado al orco, felicidades!")
                print("¡Recibirás 50 puntos de experiencia!")
                jugador.asignar_estado(50)
                orco.asignar_estado(-30) 
            else:
                print("¡Oh no! ¡El orco te ha ganado!")
                if jugador.experiencia == 0:  
                    print("Has perdido y no has ganado puntos de experiencia en esta ronda.")
                else: 
                    print("¡Has perdido 30 puntos de experiencia!")
                    jugador.asignar_estado(-30)
                orco.asignar_estado(50)  

            orco.experiencia = max(0, orco.experiencia)

            print(jugador.obtener_estado())
            print(orco.obtener_estado())

            seguir_jugando = input("¿Deseas seguir jugando? (s/n): ").lower()
            if seguir_jugando != 's':
                jugando = False
                print("\n¡Gracias por jugar a Gran Fantasía! ¡Hasta la próxima!")  

        else:  # Huir
            print("¡Has huido! El orco ha quedado atrás.")
            jugando = False
            print("\n¡Gracias por jugar a Gran Fantasía! ¡Hasta la próxima!")

if __name__ == "__main__":
    main()