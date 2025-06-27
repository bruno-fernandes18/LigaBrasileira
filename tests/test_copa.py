from core.entities.copa import Copa
from core.entities.time import Time


def test_copa_gera_chave_datas():
    copa = Copa('Copa', 2023)
    times = [Time(str(i), str(i), 1900, 'X', 'Y') for i in range(4)]
    copa.times = times
    data_inicio = copa.calendario.data_inicio
    copa.gerar_calendario()
    assert len(copa.partidas) == 3
    datas = [p.data for p in copa.calendario.partidas]
    assert datas[0] == data_inicio
    for d1, d2 in zip(datas, datas[1:]):
        assert (d2 - d1).days >= 3
