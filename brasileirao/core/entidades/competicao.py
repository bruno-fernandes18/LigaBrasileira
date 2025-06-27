from typing import List
from .time import Time
from .partida import Partida
from .calendario import Calendario

class Competicao:
    def __init__(self, nome: str, temporada: int):
        self.nome = nome
        self.temporada = temporada
        self.times: List[Time] = []
        self.partidas: List[Partida] = []
        self.classificacao: List[Time] = []
        self.artilharia = []
        self.assistencias = []
        self.dependente_de = None
        self.calendario = Calendario()
        self.trofeu = None
        self.concluida = False

    def adicionar_time(self, time: Time):
        self.times.append(time)

    def gerar_calendario(self):
        pass

    def simular_partidas(self):
        for partida in self.partidas:
            if not partida.concluida:
                partida.simular()

    def definir_campeao(self, time: Time):
        time.titulos += 1
        if self.trofeu:
            self.trofeu.conceder(time)
