from typing import List
from ..entidades.jogador import Jogador
from ..enums.posicao import Posicao


def atualizar_regens(jogadores: List[Jogador]) -> List[Jogador]:
    """Gera ou remove regens mantendo aproximadamente 1000 aposentados."""
    ativos = [j for j in jogadores if not j.aposentado]
    aposentados = [j for j in jogadores if j.aposentado]
    if len(aposentados) >= 1000:
        excesso = len(aposentados) - 999
        for j in aposentados[:excesso]:
            jogadores.remove(j)
    else:
        faltantes = 1000 - len(aposentados)
        posicao = ativos[0].posicao if ativos else Posicao.ATACANTE
        for _ in range(faltantes):
            jogadores.append(Jogador("Regen", 17, "Brasil", posicao))
    return jogadores
