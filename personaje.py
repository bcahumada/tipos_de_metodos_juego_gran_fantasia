class Personaje:
    """
    Representa a un personaje en el juego Gran Fantasía.

    Atributos:
        nombre (str): Nombre del personaje.
        nivel (int): Nivel actual del personaje (inicializado en 1).
        experiencia (int): Puntos de experiencia actuales del personaje (inicializado en 0).
    """
    def __init__(self, nombre):
        """
        Inicializa un nuevo personaje.

        Args:
            nombre (str): Nombre del personaje.
        """
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def obtener_estado(self):
        """
        Devuelve una cadena con el estado actual del personaje (nombre, nivel, experiencia).

        Returns:
            str: Estado del personaje.
        """
        return f"NOMBRE: {self.nombre}     NIVEL: {self.nivel}     EXP: {self.experiencia}"

    def asignar_estado(self, nueva_experiencia):
        """
        Actualiza la experiencia del personaje y ajusta el nivel si es necesario.

        Args:
            nueva_experiencia (int): Puntos de experiencia a añadir (pueden ser negativos).
        """
        self.experiencia += nueva_experiencia  

        # Ajustar nivel y experiencia
        while True:
            if self.experiencia >= 100:
                self.nivel += 1
                self.experiencia -= 100
            elif self.experiencia < 0 and self.nivel > 1:
                self.nivel -= 1
                self.experiencia += 100
            else:
                break 

        self.experiencia = max(0, self.experiencia)  

    def __gt__(self, otro):
        """Compara si el nivel de este personaje es mayor al de otro."""
        return self.nivel > otro.nivel

    def __lt__(self, otro):
        """Compara si el nivel de este personaje es menor al de otro."""
        return self.nivel < otro.nivel

    def __eq__(self, otro):
        """Compara si el nivel de este personaje es igual al de otro."""
        return self.nivel == otro.nivel

    def probabilidad_ganar(self, otro):
        """
        Calcula la probabilidad de ganar de este personaje contra otro.

        Args:
            otro (Personaje): El otro personaje con el que se compara.

        Returns:
            float: Probabilidad de ganar (entre 0.0 y 1.0).
        """
        if self > otro:
            return 0.66
        elif self < otro:
            return 0.33
        else:
            return 0.50

    def dialogo_enfrentamiento(self, probabilidad, oponente): 
        """
        Muestra el diálogo de enfrentamiento al jugador y obtiene su elección.

        Args:
            probabilidad (float): Probabilidad de ganar del jugador.
            oponente (Personaje): El personaje al que se enfrenta el jugador.

        Returns:
            int: Elección del jugador (1 para atacar, 2 para huir).
        """
        print(f"\n¡Oh no!, ¡Ha aparecido un {oponente.nombre}!")
        print(f"\nCon tu nivel actual, tienes {probabilidad * 100:.1f}% de probabilidades de ganarle al {oponente.nombre}.")
        print(f"Si ganas, ganarás 50 puntos de experiencia y el {oponente.nombre} perderá 30.")
        print(f"Si pierdes, perderás 30 puntos de experiencia y el {oponente.nombre} ganará 50.")
        while True:
            opcion = input("\n¿Qué deseas hacer?\n1. Atacar\n2. Huir\n")
            if opcion in ["1", "2"]:
                return int(opcion)
            else:
                print("\nOpción inválida. Por favor ingrese 1 o 2.")