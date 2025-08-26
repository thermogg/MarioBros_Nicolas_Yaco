from Personajes.Personaje import Personaje
class Enemigo(Personaje):
    def __init__(self, nombre, posicionX, posicionY, vidas=1):
        super().__init__(nombre, posicionX, posicionY, vidas)
        self._poderes = []

    def atacar(self, objetivo, dano=1):
        print(f"{self._Personaje__nombre} ataca a {objetivo._Personaje__nombre}!")
        objetivo.recibir_dano(dano)

    def recibir_dano(self, dano):
        if hasattr(Personaje, 'lanzar_fuego'):
            Personaje.lanzar_fuego = dano
        elif hasattr(Personaje, 'lanzar_hielo'):
            Personaje.lanzar_hielo = dano
        self._vidas -= dano
        if self._vidas <= 0:
            print(f"{self._Personaje__nombre} ha sido derrotado!")  
    
  
        