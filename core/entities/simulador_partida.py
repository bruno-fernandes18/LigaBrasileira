"""Simulador de partida simples."""

import random
from .partida import Partida
from ..enums.fase_partida import FasePartida
from ..systems.narrador import narrar
from ..systems.sistema_eventos import registrar_gol
from .time import Time


def calcula_numero_de_fases() -> int:
    """Retorna o limite de fases de uma partida simples."""
    return 20


def rolar_meio_campo(simulador: "SimuladorPartida") -> None:
    """Define posse de bola no meio campo."""
    simulador.subphase = 1
    simulador.phase += 1
    simulador.partida.fases.append(FasePartida.MEIO_CAMPO)

    roll_casa = random.random() * simulador.modifier_casa
    roll_visitante = random.random() * simulador.modifier_visitante
    simulador.possession = (
        simulador.partida.time_casa
        if roll_casa >= roll_visitante
        else simulador.partida.time_visitante
    )


def rolar_ataque(simulador: "SimuladorPartida") -> bool:
    """Resolve a tentativa de ataque."""
    simulador.subphase = 2
    simulador.phase += 1
    simulador.partida.fases.append(FasePartida.ATAQUE)

    ataque = random.random() * (
        simulador.modifier_casa
        if simulador.possession == simulador.partida.time_casa
        else simulador.modifier_visitante
    )
    defesa = random.random()
    if ataque < defesa:
        simulador.possession = (
            simulador.partida.time_visitante
            if simulador.possession == simulador.partida.time_casa
            else simulador.partida.time_casa
        )
        return False
    return True


def chutar_gol(simulador: "SimuladorPartida") -> float:
    """Realiza o chute ao gol e retorna sua força."""
    simulador.subphase = 3
    simulador.phase += 1
    simulador.partida.fases.append(FasePartida.GOL)
    return random.random() * (
        simulador.modifier_casa
        if simulador.possession == simulador.partida.time_casa
        else simulador.modifier_visitante
    )


def defesa_goleiro(simulador: "SimuladorPartida", chute: float) -> None:
    """Avalia a defesa do goleiro e registra gol se necessário."""
    simulador.subphase = 4
    simulador.phase += 1
    simulador.partida.fases.append(FasePartida.DEFESA)

    defesa = random.random()
    if chute > defesa:
        if simulador.possession == simulador.partida.time_casa:
            simulador.partida.placar_casa += 1
            _registrar_gol(simulador.partida.time_casa)
        else:
            simulador.partida.placar_visitante += 1
            _registrar_gol(simulador.partida.time_visitante)
    else:
        simulador.possession = (
            simulador.partida.time_visitante
            if simulador.possession == simulador.partida.time_casa
            else simulador.partida.time_casa
        )


def _registrar_gol(time: Time) -> None:
    """Soma um gol para um jogador aleatório do ``time``."""
    if not time.jogadores:
        return
    jogador = random.choice(time.jogadores)
    jogador.gols += 1

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
        """Executa até 20 fases alternando meio‑campo, ataque e finalizações."""
        narrar(
            f"Inicio da partida: {self.partida.time_casa.nome} x {self.partida.time_visitante.nome}",
            self.partida,
        )
        limite = calcula_numero_de_fases()
        while self.phase < limite:
            rolar_meio_campo(self)
            if self.phase >= limite:
                break
            if not rolar_ataque(self):
                continue
            if self.phase >= limite:
                break
            chute = chutar_gol(self)
            if self.phase >= limite:
                break
            defesa_goleiro(self, chute)
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
                time = self.partida.time_casa
            else:
                self.partida.placar_visitante += 1
                narrar(f"GOL do {self.partida.time_visitante.nome}!", self.partida)
                time = self.partida.time_visitante
            if time.jogadores:
                marcador = random.choice(time.jogadores)
                assist = None
                if len(time.jogadores) > 1:
                    candidatos = [j for j in time.jogadores if j is not marcador]
                    if candidatos:
                        assist = random.choice(candidatos)
                registrar_gol(marcador, assist)
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
