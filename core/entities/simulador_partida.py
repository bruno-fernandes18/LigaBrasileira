"""Simulador de partida simples."""

import random
from .partida import Partida
from ..enums.fase_partida import FasePartida

class SimuladorPartida:
    """Executa uma simulação simplificada de partida."""

    def __init__(self, partida: Partida) -> None:
        self.partida = partida
        self.phase = 0
        self.subphase = 0
        self.possession = random.choice([partida.time_casa, partida.time_visitante])
        self.modifier_casa = 1.1
        self.modifier_visitante = 1.0

    def simular(self) -> None:
        """Executa três subfases: meio-campo, ataque e defesa."""
        for _ in range(90 // 30):
            self.phase += 1
            self._meio_campo()
            self._ataque()
            self._defesa()
        self.partida.concluida = True

    def _meio_campo(self):
        self.subphase = 1
        self.partida.fases.append(FasePartida.MEIO_CAMPO)

    def _ataque(self):
        self.subphase = 2
        self.partida.fases.append(FasePartida.ATAQUE)
        if random.random() < 0.1:
            if self.possession == self.partida.time_casa:
                self.partida.placar_casa += 1
            else:
                self.partida.placar_visitante += 1
            self.partida.fases.append(FasePartida.GOL)

    def _defesa(self):
        self.subphase = 3
        self.partida.fases.append(FasePartida.DEFESA)
        self.possession = self.partida.time_visitante if self.possession == self.partida.time_casa else self.partida.time_casa
