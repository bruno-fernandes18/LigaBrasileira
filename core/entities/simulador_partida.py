"""Simulador de partida com fases detalhadas."""

from __future__ import annotations

import random

from .partida import Partida
from ..enums.fase_partida import FasePartida
from ..enums.estilo_tatico import EstiloTatico
from ..systems.narrador import narrar
from ..systems.sistema_eventos import registrar_gol
from .time import Time

MAX_PHASES = 20
MIN_ROLL = 0
MAX_ROLL = 40


def calcula_numero_de_fases() -> int:
    """Retorna o limite de fases de uma partida simples."""
    return MAX_PHASES


def _registrar_gol(time: Time) -> None:
    """Soma um gol a um jogador aleatorio."""
    if not time.jogadores:
        return
    jogador = random.choice(time.jogadores)
    registrar_gol(jogador)


class SimuladorPartida:
    """Executa uma simulacao simplificada de partida."""

    def __init__(self, partida: Partida) -> None:
        self.partida = partida
        self.phase = 0
        self.subphase = 0
        self.possession = random.choice([partida.time_casa, partida.time_visitante])

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def simular(self) -> None:
        """Executa ate 20 fases alternando subfases."""
        """Executa até 20 fases alternando meio-campo, ataque e finalizações."""
        narrar(
            f"Inicio da partida: {self.partida.time_casa.nome} x {self.partida.time_visitante.nome}",
            self.partida,
        )
        while self.phase < MAX_PHASES:
            self._meio_campo()
            if self.phase >= MAX_PHASES:
                break
            if not self._ataque():
                continue
            if self.phase >= MAX_PHASES:
                break
            chute = self._gol()
            if self.phase >= MAX_PHASES:
                break
            self._defesa(chute)
        limite = calcula_numero_de_fases()
        while self.phase < limite:
            rolar_meio_campo(self)
            if self.phase >= limite:
                break
            if rolar_ataque(self):
                if self.phase >= limite:
                    break
                chute = chutar_gol(self)
                if self.phase >= limite:
                    break
                defesa_goleiro(self, chute)
        self.partida.concluida = True

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _roll(self, team: Time, purpose: str) -> int:
        mod = team.sorte // 4
        tecnico = team.tecnico
        if tecnico:
            estilo = tecnico.estilo_tatico
            if purpose == "meio" and estilo == EstiloTatico.POSSE_BOLA:
                mod += 3
            if purpose == "ataque":
                if estilo == EstiloTatico.OFENSIVO:
                    mod += 5
                if estilo == EstiloTatico.CONTRA_ATAQUE:
                    mod += 3
            if purpose == "defesa" and estilo == EstiloTatico.DEFENSIVO:
                mod += 5
        roll = random.randint(MIN_ROLL, MAX_ROLL) + mod
        roll = max(MIN_ROLL, min(MAX_ROLL, roll))
        if team.sorte > 15:
            extra = random.randint(MIN_ROLL, MAX_ROLL) + mod
            extra = max(MIN_ROLL, min(MAX_ROLL, extra))
            if extra > roll:
                roll = extra
        return roll

    def _meio_campo(self) -> None:
        self.subphase = 1
        self.phase += 1
        self.partida.fases.append(FasePartida.MEIO_CAMPO)
        casa = self.partida.time_casa
        visitante = self.partida.time_visitante
        roll_casa = self._roll(casa, "meio")
        roll_visitante = self._roll(visitante, "meio")
        self.possession = casa if roll_casa >= roll_visitante else visitante

    def _ataque(self) -> bool:
        self.subphase = 2
        self.phase += 1
        self.partida.fases.append(FasePartida.ATAQUE)
        atacante = self.possession
        defensor = self.partida.time_visitante if atacante == self.partida.time_casa else self.partida.time_casa
        ataque = self._roll(atacante, "ataque")
        defesa = self._roll(defensor, "defesa")
        if ataque <= defesa or ataque == MIN_ROLL:
            self.possession = defensor
            return False
        return True

    def _gol(self) -> int:
        self.subphase = 3
        self.phase += 1
        self.partida.fases.append(FasePartida.GOL)
        return self._roll(self.possession, "ataque")

    def _defesa(self, chute: int) -> None:
        self.subphase = 4
        self.phase += 1
        self.partida.fases.append(FasePartida.DEFESA)
        defensor = self.partida.time_visitante if self.possession == self.partida.time_casa else self.partida.time_casa
        defesa = self._roll(defensor, "defesa")
        if chute > defesa and chute > MIN_ROLL:
            if self.possession == self.partida.time_casa:
                self.partida.placar_casa += 1
                _registrar_gol(self.partida.time_casa)
            else:
                self.partida.placar_visitante += 1
                _registrar_gol(self.partida.time_visitante)
        else:
            self.possession = defensor
            else:
                self.partida.placar_visitante += 1
            time = self.possession
            if time.jogadores:
                marcador = random.choice(time.jogadores)
                registrar_gol(marcador)
                assist = None
                if len(time.jogadores) > 1:
                    candidatos = [j for j in time.jogadores if j is not marcador]
                    if candidatos:
                        assist = random.choice(candidatos)
                registrar_gol(marcador, assist)
            narrar(f"GOL do {time.nome}!", self.partida)
        else:
            self.possession = (
                self.partida.time_visitante
                if self.possession == self.partida.time_casa
                else self.partida.time_casa
            )
        self._verificar_cartoes()

    def _verificar_cartoes(self) -> None:
        """Sorteia aplicação de cartões aleatoriamente."""
        chance = random.random()
        if chance < 0.02:
            narrar(f"Cartão amarelo para {self.possession.nome}", self.partida)
        elif chance < 0.025:
            narrar(f"Cartão vermelho para {self.possession.nome}", self.partida)

