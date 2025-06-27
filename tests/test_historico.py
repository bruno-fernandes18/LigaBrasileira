import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from brasileirao.persistence.history import Historico, TemporadaHistorico


def test_adicionar_temporada():
    h = Historico()
    t = TemporadaHistorico(2023)
    h.adicionar_temporada(t)
    assert h.temporadas[0] is t
