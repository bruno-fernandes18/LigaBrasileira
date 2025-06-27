from ..data.historico import Historico

class HistoryManager:
    def __init__(self):
        self.historico = Historico()

    def adicionar_temporada(self, temporada: dict):
        self.historico.adicionar_temporada(temporada)

    def obter_sala_trofeus(self, time: str):
        return self.historico.obter_trofeus_time(time)

    def obter_detalhes_temporada(self, ano: int):
        return self.historico.obter_detalhes_temporada(ano)
