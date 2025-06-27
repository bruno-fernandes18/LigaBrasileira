from __future__ import annotations

"""Simulação detalhada de partidas.

Regras básicas implementadas:
- Até 0–20 fases, definidas dinamicamente por sorte e qualidade.
- Sub‑fases: MEIO_CAMPO → (opcional) ATAQUE → (opcional) FINALIZAÇÃO.
- Rolagens consideram atributos de qualidade, sorte e estilo tático.
- Gols e assistências são registrados via sistema de eventos.
- Narrador descreve cada acontecimento importante.
"""

from random import randint, random, choice
from typing import Callable

from core.enums.estilo_tatico import EstiloTatico
from core.enums.fase_partida import FasePartida
from core.systems.narrador import narrar
from core.systems.sistema_eventos import registrar_gol
from core.entities.partida import Partida
from core.entities.time import Time

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
MAX_PHASES = 20
MIN_ROLL, MAX_ROLL = 0, 40
MARGEM_MEIO = 6  # Diferença necessária para progredir ataque
MARGEM_ATAQUE = 8  # Diferença necessária p/ chance clara de gol

# ---------------------------------------------------------------------------
# Funções utilitárias
# ---------------------------------------------------------------------------

def calcula_numero_de_fases(time_casa: Time, time_visitante: Time) -> int:
    """Define o número de fases (0–20) usando sorte & qualidade."""
    base = randint(0, MAX_PHASES)
    dif_sorte = abs(time_casa.sorte - time_visitante.sorte)
    if dif_sorte < 5:
        return base

    lucky = time_casa if time_casa.sorte > time_visitante.sorte else time_visitante
    unlucky = time_visitante if lucky is time_casa else time_casa
    dif_qual = int(abs(lucky.qualidade_geral - unlucky.qualidade_geral))

    if lucky.qualidade_geral < unlucky.qualidade_geral:
        base -= min(dif_qual, lucky.sorte)
    else:
        base += dif_qual
    return max(1, min(MAX_PHASES, base))


def _rolar(
    time: Time,
    proposito: str,  # "meio", "ataque" ou "defesa"
    estilo_bonus: dict[str, EstiloTatico | None],
) -> int:
    """Rola d20 + atributos + sorte + bônus de estilo."""
    sorte_bonus = time.sorte // 4
    valor_base = randint(MIN_ROLL, 20)

    # Qualidades básicas
    if proposito == "meio":
        valor_base += int(time.media_meio + time.media_ataque * 0.5)
    elif proposito == "ataque":
        valor_base += int(time.media_ataque + time.media_meio * 0.5)
    else:  # defesa
        valor_base += int(time.media_defesa + time.media_meio * 0.5)

    # Estilo tático do técnico
    tecnico = time.tecnico
    if tecnico:
        if proposito == "meio" and tecnico.estilo_tatico == EstiloTatico.POSSE_BOLA:
            valor_base = max(valor_base, randint(MIN_ROLL, 20) + valor_base)
        if proposito == "ataque" and tecnico.estilo_tatico == EstiloTatico.OFENSIVO:
            valor_base = max(valor_base, randint(MIN_ROLL, 20) + valor_base)
        if proposito == "defesa" and tecnico.estilo_tatico == EstiloTatico.DEFENSIVO:
            valor_base = max(valor_base, randint(MIN_ROLL, 20) + valor_base)

    total = valor_base + sorte_bonus
    # Sorte 20 → reroll vantagem
    if time.sorte == 20:
        total = max(total, randint(MIN_ROLL, 20) + sorte_bonus)
    return max(MIN_ROLL, min(MAX_ROLL, total))


def _marcar_gol(time: Time) -> None:
    """Sorteia artilheiro e (talvez) assistente, registra estatísticas."""
    if not time.jogadores:
        return
    atacantes = sorted(time.jogadores, key=lambda j: j.qualidade_ataque, reverse=True)[:3]
    goleador = choice(atacantes or time.jogadores)

    assist = None
    if random() < 0.5:  # 50 % chance de assistência
        meias = sorted(time.jogadores, key=lambda j: j.qualidade_meio_campo, reverse=True)[:3]
        assist = choice([m for m in meias if m is not goleador] or [goleador])

    registrar_gol(goleador, assist)

# ---------------------------------------------------------------------------
# Simulador
# ---------------------------------------------------------------------------

class SimuladorPartida:
    """Executa simulação detalhada de uma partida."""

    def __init__(self, partida: Partida) -> None:
        self.partida = partida
        self.fases_max = calcula_numero_de_fases(partida.time_casa, partida.time_visitante)
        self.fase_atual = 0
        self.posse: Time = choice([partida.time_casa, partida.time_visitante])

    # ----------------------------------------
    # Ciclo principal
    # ----------------------------------------
    def simular(self) -> None:
        narrar(
            f"Início: {self.partida.time_casa.nome} x {self.partida.time_visitante.nome}",
            self.partida,
        )

        while self.fase_atual < self.fases_max:
            self._fase_meio_campo()
            if self.fase_atual >= self.fases_max:
                break
            if not self._fase_ataque():  # Defesa anulou → nova fase
                continue
            if self.fase_atual >= self.fases_max:
                break
            self._fase_finalizacao()

        narrar(
            f"Fim: {self.partida.time_casa.nome} {self.partida.placar_casa} x {self.partida.placar_visitante} {self.partida.time_visitante.nome}",
            self.partida,
        )
        self.partida.concluida = True

    # ----------------------------------------
    # Fases internas
    # ----------------------------------------
    def _fase_meio_campo(self) -> None:
        self.fase_atual += 1
        self.partida.fases.append(FasePartida.MEIO_CAMPO)

        adversario = (
            self.partida.time_visitante
            if self.posse is self.partida.time_casa
            else self.partida.time_casa
        )

        r1 = _rolar(self.posse, "meio", {})
        r2 = _rolar(adversario, "meio", {})

        if abs(r1 - r2) < MARGEM_MEIO:
            narrar("Disputa acirrada no meio‑campo, ninguém progride.", self.partida)
            return  # meio‑campo continuará na próxima fase

        if r2 > r1:
            self.posse = adversario
        narrar(f"{self.posse.nome} domina o meio‑campo.", self.partida)

    def _fase_ataque(self) -> bool:
        self.fase_atual += 1
        self.partida.fases.append(FasePartida.ATAQUE)

        defensor = (
            self.partida.time_visitante
            if self.posse is self.partida.time_casa
            else self.partida.time_casa
        )

        r_atk = _rolar(self.posse, "ataque", {})
        r_def = _rolar(defensor, "defesa", {})

        if r_atk - r_def < MARGEM_ATAQUE:
            narrar("Defesa intercepta! Posse trocada.", self.partida)
            self.posse = defensor
            return False

        narrar("Chance clara de gol!", self.partida)
        return True

    def _fase_finalizacao(self) -> None:
        self.fase_atual += 1
        self.partida.fases.append(FasePartida.GOL)
        defensor = (
            self.partida.time_visitante
            if self.posse is self.partida.time_casa
            else self.partida.time_casa
        )

        chute = _rolar(self.posse, "ataque", {})
        defesa = _rolar(defensor, "defesa", {}) + 8  # bônus fixo goleiro

        if chute > defesa:
            # Gol!
            if self.posse is self.partida.time_casa:
                self.partida.placar_casa += 1
            else:
                self.partida.placar_visitante += 1
            _marcar_gol(self.posse)
            narrar(f"GOL do {self.posse.nome}!", self.partida)
        else:
            narrar("Defesa espetacular!", self.partida)

        # Após finalização, posse do adversário
        self.posse = defensor
