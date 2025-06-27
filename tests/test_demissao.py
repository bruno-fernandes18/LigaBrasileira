from core.entities.time import Time
from core.entities.tecnico import Tecnico
from core.systems.sistema_eventos import verificar_demissao_tecnicos


def test_verificar_demissao_tecnicos():
    t = Time('A', 'A', 1900, 'X', 'Y')
    coach = Tecnico('Tec', 50, 'BR')
    t.tecnico = coach
    coach.time = t
    coach.derrotas_consecutivas = 5
    verificar_demissao_tecnicos([t])
    assert t.tecnico is None
