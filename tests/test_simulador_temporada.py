from datetime import datetime
import random

from simulation.temporada import SimuladorTemporada
from core.entities.competicao import Competicao
from core.entities.time import Time
from core.entities.partida import Partida
from core.entities.jogador import Jogador
from core.enums.posicao import Posicao


def test_executar_rodada_e_transferencia():
    random.seed(0)
    t1 = Time('A', 'A', 1900, 'X', 'Y')
    t2 = Time('B', 'B', 1900, 'X', 'Y')

    j1 = Jogador('J1', 20, 'BR', Posicao.ATACANTE)
    j1.qualidade_geral = 10
    j1.potencial = 10
    j1.time = t1
    t1.jogadores.append(j1)

    j2 = Jogador('J2', 21, 'BR', Posicao.MEIA)
    j2.qualidade_geral = 10
    j2.potencial = 10
    j2.time = t2
    t2.jogadores.append(j2)

    t1.orcamento = j2.valor_mercado() + 1_000_000
    t2.orcamento = 0

    comp = Competicao('Teste', 2023)
    comp.times = [t1, t2]
    partida = Partida(t1, t2, 1, datetime.now())
    comp.partidas = [partida]

    sim = SimuladorTemporada([comp])
    sim.executar_rodada()

    assert partida.concluida
    assert len(t1.jogadores) == 2
    assert len(t2.jogadores) == 0
    assert sim.rodada_atual == 2
