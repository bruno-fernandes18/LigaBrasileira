"""Sistema financeiro."""

from __future__ import annotations

from ..entities.time import Time
from ..entities.jogador import Jogador
from .sistema_regens import regenerar_jogadores


def pagar_salarios_semanais(times: list[Time]) -> None:
    """Deduz despesas salariais do orçamento e sinaliza falência."""
    for time in times:
        time.orcamento -= time.despesas_salariais
        if time.orcamento < 0 and not time.bancarrota:
            time.bancarrota = True


def resolver_bancarrota(time: Time, outros_times: list[Time]) -> None:
    """Liquida o elenco de ``time`` e repõe com jovens regenerados."""

    MAX_ELENCO = 30
    MIN_ELENCO = 18

    for jogador in list(time.jogadores):
        for destino in outros_times:
            if len(destino.jogadores) < MAX_ELENCO:
                time.jogadores.remove(jogador)
                destino.jogadores.append(jogador)
                jogador.time = destino
                break

    novos: list[Jogador] = []
    regenerar_jogadores(novos)
    for regen in novos[: MAX_ELENCO]:
        if len(time.jogadores) >= MIN_ELENCO:
            break
        regen.time = time
        time.jogadores.append(regen)

    time.orcamento = 0
    time.despesas_salariais = 0
    time.bancarrota = False
