import random
from ..entidades.partida import Partida

class SimuladorPartida:
    def __init__(self, partida: Partida):
        self.partida = partida
        self.max_phases = random.randint(10, 20)

    def simular(self):
        for phase in range(self.max_phases):
            self.partida.adicionar_fase({'numero': phase})
        self.partida.finalizar()
