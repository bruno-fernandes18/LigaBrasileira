from datetime import datetime
from core.entities.competicao import Competicao
from core.entities.time import Time
from core.entities.partida import Partida


def test_simular_rodada():
    comp = Competicao('Teste', 2023)
    t1 = Time('A', 'A', 1900, 'X', 'Y')
    t2 = Time('B', 'B', 1900, 'X', 'Y')
    comp.times = [t1, t2]
    partida = Partida(t1, t2, 1, datetime.now())
    comp.partidas = [partida]
    comp.simular_rodada(1)
    assert partida.concluida
