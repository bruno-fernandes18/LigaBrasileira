import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from brasileirao.core.entidades.liga import Liga
from brasileirao.core.entidades.time import Time


def test_liga_gerar_calendario():
    liga = Liga("Teste", 2023)
    liga.adicionar_time(Time("A", "A", 1900, "A", "A"))
    liga.adicionar_time(Time("B", "B", 1900, "B", "B"))
    liga.gerar_calendario()
    assert liga.partidas
