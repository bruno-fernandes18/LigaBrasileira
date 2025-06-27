from datetime import datetime
from .time import Time
from ..enums.fase_partida import FasePartida
from ..sistemas.sound_manager import SoundManager

class Partida:
    def __init__(self, time_casa: Time, time_visitante: Time, rodada: int, data: datetime):
        self.time_casa = time_casa
        self.time_visitante = time_visitante
        self.rodada = rodada
        self.data = data
        self.placar_casa = 0
        self.placar_visitante = 0
        self.eventos = []
        self.fases = []
        self.estadio = time_casa.estadio
        self.arbitro = None
        self.concluida = False

    def adicionar_fase(self, fase):
        self.fases.append(fase)

    def finalizar(self):
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
