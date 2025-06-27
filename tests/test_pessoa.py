from core.entities.pessoa import Pessoa


def test_cometer_infracao_reduce_reputacao():
    p = Pessoa('Teste', 30, 'BR')
    p.cometer_infracao('falta', 5)
    assert p.reputacao == 10


def test_verificar_aposentadoria():
    p = Pessoa('Idoso', 70, 'BR')
    assert p.verificar_aposentadoria()
