"""Módulo que define a entidade ``Partida``."""

from datetime import datetime
from .time import Time
from ..enums.fase_partida import FasePartida
from ..sistemas.sound_manager import SoundManager

class Partida:
    """Representa um confronto entre dois times."""

    def __init__(self, time_casa: Time, time_visitante: Time, rodada: int, data: datetime) -> None:
        """Inicializa dados básicos de uma partida."""

        self.time_casa = time_casa
        self.time_visitante = time_visitante
        self.rodada = rodada
        self.data = data
        self.placar_casa = 0
        self.placar_visitante = 0
        self.eventos: list[FasePartida] = []
        self.fases = []
        self.estadio = time_casa.estadio
        self.arbitro = None
        self.concluida = False

    def adicionar_fase(self, fase: FasePartida) -> None:
        """Adiciona uma fase ao histórico da partida."""

        self.fases.append(fase)

    def finalizar(self) -> None:
        """Finaliza a partida e aplica regras de pontuação."""

        self.concluida = True
        self.time_casa.saldo_gols += self.placar_casa - self.placar_visitante
        self.time_visitante.saldo_gols += self.placar_visitante - self.placar_casa
        if self.placar_casa > self.placar_visitante:
            self.time_casa.pontos += 3
        elif self.placar_visitante > self.placar_casa:
            self.time_visitante.pontos += 3
        else:
            self.time_casa.pontos += 1
            self.time_visitante.pontos += 1
        SoundManager.play("apito_final")
