import random
from ..entidades.time import Time
from ..entidades.jogador import Jogador


def verificar_demissao_tecnicos(times: list[Time]):
    for time in times:
        if time.tecnico and time.tecnico.derrotas_consecutivas >= 5:
            time.tecnico.demitir()


def verificar_lesoes(jogadores: list[Jogador]):
    for jogador in jogadores:
        if not jogador.suspenso:
            if random.random() < 0.02:
                gravidade = random.choice([1, 2, 3, 4, 5])
                jogador.lesoes.append({'gravidade': gravidade, 'duracao': gravidade * 2})
