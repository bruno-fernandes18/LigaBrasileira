"""Rotinas de desenvolvimento de jogadores."""

from __future__ import annotations

import random

from ..entities.jogador import Jogador
from ..entities.time import Time
from ..enums.setor import Setor


def desenvolver_jogadores(time: Time) -> None:
    """Evolui levemente os atributos dos atletas do ``time``."""
    for jogador in time.jogadores:
        incremento = random.randint(0, 1)
        if jogador.posicao in Setor.DEFESA.posicoes():
            jogador.qualidade_defesa += incremento
        elif jogador.posicao in Setor.MEIO_CAMPO.posicoes():
            jogador.qualidade_meio_campo += incremento
        else:
            jogador.qualidade_ataque += incremento
        jogador.calcular_qualidade_geral()


def premiar_destaques(times: list[Time]) -> None:
    """Premia jogadores com mais gols ou assistências."""
    jogadores = [j for t in times for j in t.jogadores]
    if not jogadores:
        return
    max_gols = max(j.gols for j in jogadores)
    max_assist = max(j.assistencias for j in jogadores)
    for jogador in jogadores:
        if jogador.gols == max_gols or jogador.assistencias == max_assist:
            jogador.potencial = min(20, jogador.potencial + 1)
            jogador.reputacao = min(20, jogador.reputacao + 1)
            jogador.titulos += 1
