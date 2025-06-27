import random
from typing import List
from ..entidades.time import Time
from ..enums.setor import Setor


def contratar_jogador(time_comprador: Time, time_vendedor: Time, setor: Setor) -> bool:
    chance = 0.6 - (time_vendedor.sorte * 0.01)
    if random.random() > chance:
        return False
    jogadores = [j for j in time_vendedor.jogadores if j.posicao in setor.posicoes()]
    if not jogadores:
        return False
    jogador = max(jogadores, key=lambda j: j.qualidade_geral)
    valor = jogador.valor_mercado()
    if time_comprador.factor_orcamento * 1_000_000 > valor:
        time_vendedor.jogadores.remove(jogador)
        time_comprador.jogadores.append(jogador)
        jogador.time = time_comprador
        return True
    return False
