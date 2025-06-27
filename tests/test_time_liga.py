from core.entities.liga import Liga
from core.entities.time import Time


def test_liga_atribuida_aos_times():
    liga = Liga('Serie A', 2023)
    t1 = Time('A', 'A', 1900, 'X', 'Y')
    t2 = Time('B', 'B', 1900, 'X', 'Y')
    liga.times = [t1, t2]
    liga.gerar_calendario()
    assert t1.liga is liga
    assert t2.liga is liga
