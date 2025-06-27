"""Implementações avançadas inspiradas pelo 'Chefe Barroso'.

Este módulo contém funções e classes experimentais não utilizadas pelo
simulador padrão, mas que refletem requisitos mais complexos.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Tuple

from ..entidades.time import Time
from ..entidades.jogador import Jogador
from ..enums.posicao import Posicao
from .sound_manager import SoundManager


# ---------------------------------------------------------------------------
# SISTEMA DE PHASES
# ---------------------------------------------------------------------------

def calcular_phases(casa: Time, visitante: Time) -> int:
    """Calcula o número de fases de uma partida.

    A implementação segue a lógica sugerida no documento do Chefe Barroso.
    """
    base_phases = random.randint(0, 20)

    dif_sorte = abs(casa.sorte - visitante.sorte)
    lucky_team = casa if casa.sorte > visitante.sorte else visitante

    dif_qualidade = abs(getattr(casa, "qualidade_geral", 0) - getattr(visitante, "qualidade_geral", 0))

    if dif_sorte >= 5:
        if lucky_team == casa and getattr(casa, "qualidade_geral", 0) < getattr(visitante, "qualidade_geral", 0):
            base_phases -= min(dif_qualidade, casa.sorte)
        else:
            base_phases += min(dif_qualidade, lucky_team.sorte)

    recalculos = 0
    max_recalculos = 2 if casa.sorte == 20 else 1

    if getattr(casa, "qualidade_geral", 0) < getattr(visitante, "qualidade_geral", 0):
        if base_phases > dif_qualidade and recalculos < max_recalculos:
            base_phases = random.randint(0, 20)
            recalculos += 1
    else:
        if base_phases < dif_qualidade and recalculos < max_recalculos:
            base_phases = random.randint(0, 20)
            recalculos += 1

    return max(0, min(20, base_phases))


# ---------------------------------------------------------------------------
# SUBSISTEMA DE ROLAGENS
# ---------------------------------------------------------------------------

class Rolagem:
    """Conjunto de métodos para cálculos de rolagens em diferentes setores."""

    @staticmethod
    def _reroll(value: int, sorte: int) -> int:
        reroll_count = 2 if sorte == 20 else 1
        for _ in range(reroll_count):
            novo = random.randint(0, 20)
            if novo > value:
                value = novo
        return value

    @staticmethod
    def meio_campo(time: Time, possession: bool, modifier: int) -> Tuple[int, int]:
        roll = random.randint(0, 20)
        base_value = roll + getattr(time, "qualidade_construcao", 0)

        if getattr(time.tecnico, "estilo", None) == "TIKI_TAKA" and possession:
            rerolls = [random.randint(0, 20) for _ in range(2)]
            base_value = max(rerolls + [base_value])
        elif getattr(time.tecnico, "estilo", None) == "GEGENPRESSING" and not possession:
            rerolls = [random.randint(0, 20) for _ in range(2)]
            base_value = max(rerolls + [base_value])

        if roll < time.sorte:
            roll = Rolagem._reroll(roll, time.sorte)
            base_value = roll + getattr(time, "qualidade_construcao", 0)

        if roll == 0:
            modifier += 3
            return max(0, min(40, base_value + modifier)), modifier

        return max(0, min(40, base_value + modifier)), modifier

    # Os métodos abaixo seguem o mesmo padrão do meio_campo.
    @staticmethod
    def ataque(time: Time, possession: bool, modifier: int) -> Tuple[int, int]:
        roll = random.randint(0, 20)
        base_value = roll + getattr(time, "qualidade_ataque", 0)

        if getattr(time.tecnico, "estilo", None) == "TIKI_TAKA" and possession:
            rerolls = [random.randint(0, 20) for _ in range(2)]
            base_value = max(rerolls + [base_value])
        elif getattr(time.tecnico, "estilo", None) == "GEGENPRESSING" and not possession:
            rerolls = [random.randint(0, 20) for _ in range(2)]
            base_value = max(rerolls + [base_value])

        if roll < time.sorte:
            roll = Rolagem._reroll(roll, time.sorte)
            base_value = roll + getattr(time, "qualidade_ataque", 0)

        if roll == 0:
            modifier += 3
            return max(0, min(40, base_value + modifier)), modifier

        return max(0, min(40, base_value + modifier)), modifier

    @staticmethod
    def defesa(time: Time, possession: bool, modifier: int) -> Tuple[int, int]:
        roll = random.randint(0, 20)
        base_value = roll + getattr(time, "qualidade_defesa", 0)

        if getattr(time.tecnico, "estilo", None) == "TIKI_TAKA" and possession:
            rerolls = [random.randint(0, 20) for _ in range(2)]
            base_value = max(rerolls + [base_value])
        elif getattr(time.tecnico, "estilo", None) == "GEGENPRESSING" and not possession:
            rerolls = [random.randint(0, 20) for _ in range(2)]
            base_value = max(rerolls + [base_value])

        if roll < time.sorte:
            roll = Rolagem._reroll(roll, time.sorte)
            base_value = roll + getattr(time, "qualidade_defesa", 0)

        if roll == 0:
            modifier += 3
            return max(0, min(40, base_value + modifier)), modifier

        return max(0, min(40, base_value + modifier)), modifier

    @staticmethod
    def gol(time: Time, possession: bool, modifier: int) -> Tuple[int, int]:
        roll = random.randint(0, 20)
        base_value = roll + getattr(time, "qualidade_ataque", 0)

        if roll < time.sorte:
            roll = Rolagem._reroll(roll, time.sorte)
            base_value = roll + getattr(time, "qualidade_ataque", 0)

        if roll == 0:
            modifier += 3
            return max(0, min(40, base_value + modifier)), modifier

        return max(0, min(40, base_value + modifier)), modifier

    @staticmethod
    def goleiro(time: Time, possession: bool, modifier: int) -> Tuple[int, int]:
        base_value = getattr(time, "qualidade_defesa", 0) + modifier
        return max(0, min(40, base_value)), modifier


# ---------------------------------------------------------------------------
# SISTEMA DE BANCARROTA
# ---------------------------------------------------------------------------

@dataclass
class LigaSimples:
    times: List[Time]


class JogadorBase:
    """Gera jogadores simples para composição do elenco."""

    @staticmethod
    def gerar() -> Jogador:
        posicao = random.choice(list(Posicao))
        jogador = Jogador(f"Base {random.randint(1, 1000)}", 18, "BR", posicao)
        jogador.calcular_qualidade_geral()
        return jogador


def processar_bancarrota(time: Time, liga: LigaSimples) -> None:
    times_ricos = sorted(liga.times, key=lambda t: t.orcamento, reverse=True)

    for jogador in list(time.jogadores):
        transferido = False
        for t in times_ricos:
            if t == time:
                continue
            if hasattr(t, "obter_posicoes_necessarias") and hasattr(t, "verificar_vagas"):
                posicoes = t.obter_posicoes_necessarias()
                if jogador.posicao in posicoes and t.verificar_vagas(jogador.posicao):
                    t.jogadores.append(jogador)
                    time.jogadores.remove(jogador)
                    transferido = True
                    break
        if not transferido:
            times_pobres = [t for t in liga.times if t != time]
            if times_pobres:
                times_pobres[-1].jogadores.append(jogador)
                time.jogadores.remove(jogador)

    while len(time.jogadores) < 11:
        novo_jogador = JogadorBase.gerar()
        time.jogadores.append(novo_jogador)

    time.factor_torcida = max(1, time.factor_torcida - 5)
    time.factor_orcamento = 1
    time.sorte = max(5, time.sorte - 3)
    setattr(time, "reputacao", 0)


# ---------------------------------------------------------------------------
# CALENDÁRIO AVANÇADO
# ---------------------------------------------------------------------------

class CalendarioApocalipticoError(Exception):
    pass


class EventoCalendario:
    def __init__(self, data: datetime, id: str) -> None:
        self.data = data
        self.id = id


class CalendarioAvancado:
    def __init__(self) -> None:
        self.eventos: List[EventoCalendario] = []

    def adicionar_evento(self, evento: EventoCalendario) -> None:
        self.eventos.append(evento)
        self.eventos.sort(key=lambda e: e.data)

    def gerar_calendario(self, competicoes: List) -> None:
        competicoes.sort(key=lambda c: 0 if getattr(c, "is_liga", False) else 1)
        data_atual = datetime(2023, 1, 1)

        for comp in competicoes:
            for _ in range(getattr(comp, "num_rodadas", 0)):
                while True:
                    data_valida = True
                    for evento_existente in self.eventos:
                        if abs((data_atual - evento_existente.data).days) < 3:
                            data_valida = False
                            break
                    if data_valida:
                        break
                    data_atual += timedelta(days=1)

                partidas_rodada = []
                if hasattr(comp, "obter_partidas_rodada"):
                    partidas_rodada = comp.obter_partidas_rodada()
                for partida in partidas_rodada:
                    partida.data = data_atual
                    self.adicionar_evento(EventoCalendario(data_atual, getattr(partida, "id", "partida")))
                data_atual += timedelta(weeks=1)

        self.validar_calendario()

    def validar_calendario(self) -> None:
        for i, evento in enumerate(self.eventos):
            if evento.data < datetime(2023, 1, 1) or evento.data > datetime(2023, 12, 31):
                raise CalendarioApocalipticoError(f"Evento {evento.id} fora do período!")
            if i > 0:
                dias_entre = (evento.data - self.eventos[i - 1].data).days
                if dias_entre < 3:
                    raise CalendarioApocalipticoError(
                        f"Intervalo inválido entre {evento.id} e anterior!"
                    )


# ---------------------------------------------------------------------------
# SALA DE TROFÉUS
# ---------------------------------------------------------------------------

class SalaTrofeus:
    def __init__(self, canvas=None) -> None:
        self.canvas = canvas
        self.confirmacao_usuario = False

    def piscar_botao(self, nome: str) -> None:
        pass  # placeholder para interface

    def adicionar_trofeu(self, time: Time, trofeu) -> None:
        time.trofeus.append(trofeu)
        if hasattr(time, "historico"):
            time.historico.adicionar_conquista(trofeu)
        self.tocar_hino(time)
        self.exibir_animacao(trofeu)
        while not self.confirmacao_usuario:
            if hasattr(SoundManager, "pygame") and SoundManager.pygame:
                SoundManager.pygame.time.wait(500)  # pragma: no cover - depende do pygame
            self.piscar_botao("Nova Temporada")

    def tocar_hino(self, time: Time) -> None:
        try:
            SoundManager.play(f"hinos/{time.nome}.mp3")
        except Exception:
            SoundManager.play("hinos/padrao.mp3")

    def exibir_animacao(self, trofeu) -> None:
        for frame in getattr(trofeu, "animacao_frames", []):
            if self.canvas:
                self.canvas.delete("all")
                self.canvas.create_image(frame, tags="trofeu")
                self.canvas.update()
            if hasattr(SoundManager, "pygame") and SoundManager.pygame:
                SoundManager.pygame.time.wait(100)  # pragma: no cover

