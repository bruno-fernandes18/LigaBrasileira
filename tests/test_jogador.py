from core.entities.jogador import Jogador
from core.enums.posicao import Posicao


def test_calcular_qualidade_geral():
    j = Jogador('A', 20, 'BR', Posicao.ATACANTE)
    j.qualidade_ataque = 10
    j.qualidade_meio_campo = 5
    j.calcular_qualidade_geral()
    assert j.qualidade_geral == 8


def test_valor_mercado():
    j = Jogador('A', 20, 'BR', Posicao.ATACANTE)
    j.qualidade_geral = 10
    j.potencial = 20
    assert j.valor_mercado() > 0
