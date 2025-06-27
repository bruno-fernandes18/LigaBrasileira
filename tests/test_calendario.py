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


def test_verificar_temporada():
    cal = Calendario()
    t1 = Time('A', 'A', 1900, 'X', 'Y')
    t2 = Time('B', 'B', 1900, 'X', 'Y')
    cal.partidas = [
        Partida(t1, t2, 1, date(2023, 1, 1)),
        Partida(t1, t2, 2, date(2024, 1, 1)),
    ]
    assert not cal.verificar_temporada(2023)


def test_verificar_espacamento_times():
    cal = Calendario()
    t1 = Time('A', 'A', 1900, 'X', 'Y')
    t2 = Time('B', 'B', 1900, 'X', 'Y')
    t3 = Time('C', 'C', 1900, 'X', 'Y')
    cal.partidas = [
        Partida(t1, t2, 1, date(2023, 1, 1)),
        Partida(t1, t3, 2, date(2023, 1, 2)),
    ]
    assert not cal.verificar_espacamento_times([t1, t2, t3])
    cal.partidas[1].data = date(2023, 1, 4)
    assert cal.verificar_espacamento_times([t1, t2, t3])


def test_verificar_distribuicao_mensal():
    cal = Calendario()
    t1 = Time('A', 'A', 1900, 'X', 'Y')
    t2 = Time('B', 'B', 1900, 'X', 'Y')
    from datetime import timedelta

    for i in range(12):
        cal.partidas.append(Partida(t1, t2, i + 1, date(2023, 1, 1) + timedelta(days=i)))
    assert not cal.verificar_distribuicao_mensal()

    cal.partidas.clear()
    for m in range(1, 7):
        cal.partidas.append(Partida(t1, t2, m * 2 - 1, date(2023, m, 1)))
        cal.partidas.append(Partida(t1, t2, m * 2, date(2023, m, 15)))
    assert cal.verificar_distribuicao_mensal()
