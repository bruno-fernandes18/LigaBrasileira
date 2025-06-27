"""Histórico de temporadas."""

class TemporadaHistorico:
    """Registra informações de uma temporada."""

    def __init__(self, ano: int) -> None:
        self.ano = ano
        self.resultados = []
        self.trofeus = {}
        self.artilheiros = []

class Historico:
    """Coleção de temporadas."""

    def __init__(self) -> None:
        self.temporadas: list[TemporadaHistorico] = []

    def adicionar_temporada(self, temporada: TemporadaHistorico) -> None:
        self.temporadas.append(temporada)
