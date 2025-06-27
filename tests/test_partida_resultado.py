from datetime import datetime
from core.entities.time import Time
from core.entities.partida import Partida
from core.entities.simulador_partida import SimuladorPartida


def test_partida_simular_atualiza_pontos(monkeypatch):
    t1 = Time('A', 'A', 1900, 'X', 'Y')
    t2 = Time('B', 'B', 1900, 'X', 'Y')
    partida = Partida(t1, t2, 1, datetime.now())

    def fake_sim(self):
        self.partida.placar_casa = 3
        self.partida.placar_visitante = 1
    
    monkeypatch.setattr(SimuladorPartida, 'simular', fake_sim)
    partida.simular()

    assert t1.pontos == 3
    assert t2.pontos == 0
    assert t1.saldo_gols == 2
    assert t2.saldo_gols == -2

