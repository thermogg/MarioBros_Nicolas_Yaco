class Personaje:
    def __init__(self, nombre, posicionX=0, posicionY=0, vidas=1):
        self.__nombre = nombre
        self._posicionX = posicionX
        self._posicionY = posicionY
        self._vidas = vidas

    def moverse(self, nuevaPosicionX):
        self._posicionX = nuevaPosicionX

    def saltar(self, nuevaPosicionY):
        self._posicionY = nuevaPosicionY

    def caer(self, nuevaPosicionY):
        self._posicionY = nuevaPosicionY

    def recibir_dano(self, dano):
        self._vidas -= dano
        if self._vidas <= 0:
            print(f"{self.__nombre} ha sido derrotado!")
    
