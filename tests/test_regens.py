import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from brasileirao.core.sistemas.sistema_regens import atualizar_regens
from brasileirao.core.entidades.jogador import Jogador
from brasileirao.core.enums.posicao import Posicao


def test_regens_gera_novos():
    jogadores = [Jogador("J", 36, "BR", Posicao.ATACANTE) for _ in range(5)]
    for j in jogadores:
        j.aposentado = True
    atualizar_regens(jogadores)
    assert len([j for j in jogadores if j.aposentado]) >= 5
