from Personajes.Personaje import Personaje
class Luigi(Personaje):
    def __init__(self, nombre, posicionX, posicionY, vidas=3):
        super().__init__(nombre, posicionX, posicionY, vidas)
        self._poderes = []

    def lanzar_hielo(self):
        print(f"{self._Personaje__nombre} lanza hielo!")
        daño = 2
        return daño
    def agarrar_hongo(self):
        print(f"{self._Personaje__nombre} ha agarrado un hongo verde!")
        self._vidas += 1