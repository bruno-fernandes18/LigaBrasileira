from core.entities.time import Time
from core.entities.jogador import Jogador
from core.enums.posicao import Posicao
from core.systems.sistema_financeiro import resolver_bancarrota


def test_resolver_bancarrota_transfere_jogadores_e_adiciona_regens():
    t1 = Time('Falido', 'F', 1900, 'X', 'Y')
    t2 = Time('Saudavel', 'S', 1900, 'X', 'Y')
    j = Jogador('Craque', 20, 'BR', Posicao.ATACANTE)
    j.time = t1
    t1.jogadores.append(j)

    resolver_bancarrota(t1, [t2])

    assert j.time is t2
    assert j in t2.jogadores
    assert len(t1.jogadores) >= 1
