from datetime import datetime
from core.entities.time import Time
from core.entities.partida import Partida
from core.entities.simulador_partida import SimuladorPartida


def test_simulador_limites_e_concluida():
    p = Partida(Time('A', 'A', 1900, 'X', 'Y'), Time('B', 'B', 1900, 'X', 'Y'), 1, datetime.now())
    simulador = SimuladorPartida(p)
    simulador.simular()
    assert 0 <= simulador.phase <= 20
    assert p.concluida
