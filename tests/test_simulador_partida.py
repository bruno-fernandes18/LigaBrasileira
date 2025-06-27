from datetime import datetime

from core.entities.time import Time
from core.entities.partida import Partida
from core.entities.simulador_partida import SimuladorPartida
from core.enums.fase_partida import FasePartida


def test_simulador_limites_e_fases():
    partida = Partida(Time('A', 'A', 1900, 'X', 'Y'), Time('B', 'B', 1900, 'X', 'Y'), 1, datetime.now())
    simulador = SimuladorPartida(partida)
    simulador.simular()
    assert 0 < simulador.phase <= 20
    assert partida.concluida
    assert len(partida.fases) == simulador.phase
    assert all(f in FasePartida for f in partida.fases)

