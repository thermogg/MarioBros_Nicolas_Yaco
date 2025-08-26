from Personajes.Enemigos import Enemigo
class KoopaTroopa(Enemigo):
    def __init__(self, nombre, posicionX, posicionY, vidas=2):
        super().__init__(nombre, posicionX, posicionY, vidas)
    
    def caminar(self):
        print(f"{self._Personaje__nombre} camina lentamente.")
    
    def atacar(self, objetivo):
        super().atacar(objetivo, dano=1)

    def recibir_dano(self, dano):
        super().recibir_dano(dano)
        if self._vidas <= 0:
            print(f"{self._Personaje__nombre} ha sido derrotado!")
    
    def caparazon(self):
        if self._vidas == 1:
            print(f"{self._Personaje__nombre} se encierra en su caparazón.")