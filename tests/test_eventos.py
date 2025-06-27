from core.entities.liga import Liga
from core.entities.time import Time
from core.entities.jogador import Jogador
from core.enums.posicao import Posicao
from core.systems.sistema_eventos import registrar_gol


def test_registrar_gol_atualiza_estatisticas_e_lideres():
    liga = Liga('L', 2023)
    t = Time('A', 'A', 1900, 'X', 'Y')
    liga.times = [t]
    t.liga = liga

    j1 = Jogador('J1', 20, 'BR', Posicao.ATACANTE)
    j2 = Jogador('J2', 20, 'BR', Posicao.MEIA)
    j1.time = t
    j2.time = t
    t.jogadores = [j1, j2]

    registrar_gol(j1, j2)

    assert j1.gols == 1
    assert j2.assistencias == 1
    assert liga.artilharia[j1] == 1
    assert liga.assistencias[j2] == 1
