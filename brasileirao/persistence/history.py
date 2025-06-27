class TemporadaHistorico:
    def __init__(self, ano: int):
        self.ano = ano
        self.resultados = []
        self.trofeus = {}
        self.artilheiros = []


class Historico:
    def __init__(self):
        self.temporadas: list[TemporadaHistorico] = []

    def adicionar_temporada(self, temporada: TemporadaHistorico):
        self.temporadas.append(temporada)

    def obter_trofeus_time(self, time: str):
        return [t for t in self.temporadas if t.trofeus.get(time)]
