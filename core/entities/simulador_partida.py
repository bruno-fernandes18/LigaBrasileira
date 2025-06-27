"""Simulador de partida simples."""

import random
from .partida import Partida
from ..enums.fase_partida import FasePartida
from ..systems.narrador import narrar

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
        narrar(
            f"Inicio da partida: {self.partida.time_casa.nome} x {self.partida.time_visitante.nome}",
            self.partida,
        )
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
        narrar("Disputa no meio-campo", self.partida)
        roll_casa = random.random() * self.modifier_casa
        roll_visitante = random.random() * self.modifier_visitante
        if roll_casa >= roll_visitante:
            self.possession = self.partida.time_casa
        else:
            self.possession = self.partida.time_visitante
        self._verificar_cartoes()

    def _ataque(self) -> None:
        self.subphase = 2
        self.phase += 1
        self.partida.fases.append(FasePartida.ATAQUE)
        narrar(f"{self.possession.nome} parte para o ataque", self.partida)
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
            narrar("A defesa leva a melhor", self.partida)
        self._verificar_cartoes()
    def _gol(self) -> None:
        self.subphase = 3
        self.phase += 1
        self.partida.fases.append(FasePartida.GOL)
        narrar(f"{self.possession.nome} finaliza ao gol", self.partida)
        chute = random.random() * (
            self.modifier_casa if self.possession == self.partida.time_casa else self.modifier_visitante
        )
        defesa = random.random()
        if chute > defesa:
            if self.possession == self.partida.time_casa:
                self.partida.placar_casa += 1
                narrar(f"GOL do {self.partida.time_casa.nome}!", self.partida)
            else:
                self.partida.placar_visitante += 1
                narrar(f"GOL do {self.partida.time_visitante.nome}!", self.partida)
        else:
            self.possession = (
                self.partida.time_visitante
                if self.possession == self.partida.time_casa
                else self.partida.time_casa
            )
            narrar("A bola n\u00e3o entrou", self.partida)
        self._verificar_cartoes()

    def _verificar_cartoes(self) -> None:
        """Sorteia aplicação de cartões aleatoriamente."""
        chance = random.random()
        if chance < 0.02:
            narrar(f"Cartão amarelo para {self.possession.nome}", self.partida)
        elif chance < 0.025:
            narrar(f"Cartão vermelho para {self.possession.nome}", self.partida)
