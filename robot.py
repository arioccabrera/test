class Robot:
    def __init__(self, nombre, bateria=100, habilidades=[]):
        self.__nombre = nombre
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nombre (self):
        return self.__nombre
    @property
    def bateria (self):
        return self.__bateria
    @property
    def habilidades(self):
        return self.__habilidades

    def cargar(self):
        self.__bateria = 100

    def decir_nombre(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'Me llamo {self.__nombre}'
        return 'Estoy seco de bateria, cargame y te digo mi nombre'

    def nueva_habilidad(self, nueva, gasto):
        if self.__bateria >= gasto:
            self.__bateria -= gasto
            self.__habilidades.append(nueva)
            return f'expetaculo, aprendi{nueva}'
        return 'Estoy seco de bateria, cargame y te aprendo lo que quieras'