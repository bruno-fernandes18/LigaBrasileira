from simulation.competition.liga_segunda_divisao import LigaSegundaDivisao
from simulation.competition.liga_brasileira import LigaBrasileira
from simulation.temporada import SimuladorTemporada
from core.data.times_db import TIMES_SERIE_B
from core.entities.time import Time


def test_liga_segunda_divisao_popula_times():
    liga = LigaSegundaDivisao("B", 2023)
    assert len(liga.times) == len(TIMES_SERIE_B)
    assert all(t.nome in TIMES_SERIE_B for t in liga.times)


def test_promocao_e_rebaixamento():
    liga_a = LigaBrasileira("A", 2023)
    liga_b = LigaSegundaDivisao("B", 2023)
    liga_a.times = [Time("A1", "A1", 1900, "X", "Y"), Time("A2", "A2", 1900, "X", "Y")]
    liga_b.times = [Time("B1", "B1", 1900, "X", "Y"), Time("B2", "B2", 1900, "X", "Y")]
    for l in [liga_a, liga_b]:
        for t in l.times:
            t.liga = l
        l.classificacao = l.times[:]
    liga_a.classificacao = [liga_a.times[0], liga_a.times[1]]
    liga_b.classificacao = [liga_b.times[0], liga_b.times[1]]
    sim = SimuladorTemporada([liga_a, liga_b])
    sim.iniciar_nova_temporada(qtd_movimentacao=1)
    assert any(t.nome == "B1" for t in liga_a.times)
    assert any(t.nome == "A2" for t in liga_b.times)
