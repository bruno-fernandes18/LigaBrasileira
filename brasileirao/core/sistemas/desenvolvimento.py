from typing import List
from ..entidades.jogador import Jogador


def desenvolver_jogadores(jogadores: List[Jogador]):
    for jogador in jogadores:
        if jogador.idade < 25:
            jogador.desenvolver()
