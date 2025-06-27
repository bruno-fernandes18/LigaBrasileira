from datetime import datetime
from core.entities.liga import Liga
from core.entities.time import Time
from core.entities.partida import Partida


def test_pontos_e_classificacao():
    liga = Liga('L', 2023)
    t1 = Time('A', 'A', 1900, 'X', 'Y')
    t2 = Time('B', 'B', 1900, 'X', 'Y')
    liga.times = [t1, t2]

    # cria duas partidas manualmente
    p1 = Partida(t1, t2, 1, datetime.now())
    p2 = Partida(t2, t1, 2, datetime.now())
    liga.partidas = [p1, p2]
    liga.classificacao = [t2, t1]  # ordem invertida para testar ordenacao

    def sim1():
        p1.placar_casa = 2
        p1.placar_visitante = 0
        p1.concluida = True
    p1.simular = sim1

    liga.simular_rodada(1)
    assert t1.pontos == 3
    assert t2.pontos == 0
    assert t1.saldo_gols == 2
    assert t2.saldo_gols == -2
    assert liga.classificacao[0] == t1

    def sim2():
        p2.placar_casa = 1
        p2.placar_visitante = 0
        p2.concluida = True
    p2.simular = sim2

    liga.simular_rodada(2)
    assert t2.pontos == 3
    assert liga.classificacao[0] == t1
