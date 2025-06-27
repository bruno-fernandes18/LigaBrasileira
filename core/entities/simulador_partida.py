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
        """Executa fases limitadas em meio-campo, ataque e gol."""
        while self.phase < 20:
            self._meio_campo()
            if self.phase >= 20:
                break
            self._ataque()
            if self.phase >= 20:
                break
            self._gol()
        self.partida.concluida = True

    def _meio_campo(self) -> None:
        self.subphase = 1
        self.phase += 1
        self.partida.fases.append(FasePartida.MEIO_CAMPO)
        roll_casa = random.random() * self.modifier_casa
        roll_visitante = random.random() * self.modifier_visitante
        if roll_casa >= roll_visitante:
            self.possession = self.partida.time_casa
        else:
            self.possession = self.partida.time_visitante

    def _ataque(self) -> None:
        self.subphase = 2
        self.phase += 1
        self.partida.fases.append(FasePartida.ATAQUE)
        ataque = random.random() * (
            self.modifier_casa if self.possession == self.partida.time_casa else self.modifier_visitante
        )
        defesa = random.random()
        if ataque < defesa:
            self.possession = (
                self.partida.time_visitante
                if self.possession == self.partida.time_casa
                else self.partida.time_casa
            )

    def _gol(self) -> None:
        self.subphase = 3
        self.phase += 1
        self.partida.fases.append(FasePartida.GOL)
        chute = random.random() * (
            self.modifier_casa if self.possession == self.partida.time_casa else self.modifier_visitante
        )
        defesa = random.random()
        if chute > defesa:
            if self.possession == self.partida.time_casa:
                self.partida.placar_casa += 1
            else:
                self.partida.placar_visitante += 1
        else:
            self.possession = (
                self.partida.time_visitante
                if self.possession == self.partida.time_casa
                else self.partida.time_casa
            )
