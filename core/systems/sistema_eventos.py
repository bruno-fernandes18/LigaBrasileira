"""Sistema de eventos aleatórios."""

import random
from ..entities.time import Time
from ..entities.jogador import Jogador


def verificar_lesoes(jogadores: list[Jogador]) -> None:
    """Sorteia lesões simples."""
    for j in jogadores:
        if random.random() < 0.02:
            j.lesoes.append({'gravidade': 1, 'duracao': 2})


def verificar_demissao_tecnicos(times: list[Time]) -> None:
    """Demite técnicos com muitas derrotas."""
    for t in times:
        if t.tecnico and t.tecnico.derrotas_consecutivas >= 5:
            t.tecnico.demitir()


def registrar_gol(jogador: Jogador, assist: Jogador | None = None) -> None:
    """Atualiza estatísticas individuais e tabelas da liga."""
    jogador.gols += 1
    if assist:
        assist.assistencias += 1

    time = jogador.time
    liga = time.liga if time else None
    if liga:
        liga.artilharia[jogador] = jogador.gols
        if assist:
            liga.assistencias[assist] = assist.assistencias
