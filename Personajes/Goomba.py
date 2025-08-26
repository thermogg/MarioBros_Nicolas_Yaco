from Personajes.Enemigos import Enemigo

class Goomba(Enemigo):
    def __init__(self, nombre, posicionX, posicionY, vidas=1):
        super().__init__(nombre, posicionX, posicionY, vidas)
    
    def caminar(self):
        print(f"{self._Personaje__nombre} se acerca intimidantemente.")
    
    def atacar(self, objetivo):
        super().atacar(objetivo, dano=1)

    def recibir_dano(self, dano):
        super().recibir_dano(dano)
        if self._vidas <= 0:
            print(f"{self._Personaje__nombre} ha sido aplastado!")
    
    def saltar(self, nuevaPosicionY):
        return super().saltar(nuevaPosicionY)