"""Sistema de contratações."""

from __future__ import annotations

from ..entities.jogador import Jogador
from ..entities.time import Time


def contratar_jogador(time: Time, jogador: Jogador, valor: int, salario: int = 0) -> bool:
    """Contrata ``jogador`` para o ``time`` se houver orçamento."""
    if jogador.time is time:
        return False
    if time.orcamento < valor:
        return False
    if jogador.time:
        jogador.time.jogadores.remove(jogador)
    time.orcamento -= valor
    jogador.time = time
    time.jogadores.append(jogador)
    time.despesas_salariais += salario
    return True
