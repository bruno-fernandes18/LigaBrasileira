"""Entidade Partida."""

from datetime import datetime
from .time import Time

class Partida:
    """Representa uma partida entre dois times."""

    def __init__(self, time_casa: Time, time_visitante: Time, rodada: int, data: datetime) -> None:
        self.time_casa = time_casa
        self.time_visitante = time_visitante
        self.rodada = rodada
        self.data = data
        self.placar_casa = 0
        self.placar_visitante = 0
        self.eventos: list = []
        self.fases: list = []
        self.arbitro = None
        self.concluida = False

    def simular(self) -> None:
        """Simula a partida utilizando o simulador."""
        from .simulador_partida import SimuladorPartida
        SimuladorPartida(self).simular()
        self.concluida = True
