from core.entities.time import Time
from core.systems.sistema_financeiro import pagar_salarios_semanais


def test_pagar_salarios_semanais():
    t = Time('A', 'A', 1900, 'X', 'Y')
    t.despesas_salariais = 20_000_000
    pagar_salarios_semanais([t])
    assert t.bancarrota
