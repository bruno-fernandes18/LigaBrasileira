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
        self.resultado_aplicado = False

    def simular(self) -> None:
        """Simula a partida utilizando o simulador."""
        from .simulador_partida import SimuladorPartida
        SimuladorPartida(self).simular()
        self.concluida = True
        self.aplicar_resultado()

    def aplicar_resultado(self) -> None:
        """Atualiza pontos e saldo de gols dos times se ainda não feito."""
        if self.resultado_aplicado:
            return
        casa = self.time_casa
        visitante = self.time_visitante
        casa.saldo_gols += self.placar_casa - self.placar_visitante
        visitante.saldo_gols += self.placar_visitante - self.placar_casa
        if self.placar_casa > self.placar_visitante:
            casa.pontos += 3
        elif self.placar_casa < self.placar_visitante:
            visitante.pontos += 3
        else:
            casa.pontos += 1
            visitante.pontos += 1
        self.resultado_aplicado = True
