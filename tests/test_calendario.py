from datetime import date
from core.entities.time import Time
from core.entities.partida import Partida
from core.entities.calendario import Calendario


def test_proxima_data_disponivel():
    cal = Calendario()
    t1 = Time('A', 'A', 1900, 'X', 'Y')
    t2 = Time('B', 'B', 1900, 'X', 'Y')
    p1 = Partida(t1, t2, 1, date(2023, 1, 1))
    cal.adicionar_partida(p1)
    next_date = cal.proxima_data_disponivel(date(2023, 1, 2))
    assert (next_date - p1.data).days >= 3
