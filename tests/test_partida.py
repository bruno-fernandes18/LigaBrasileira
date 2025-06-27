import unittest
from datetime import datetime
from brasileirao.core.entidades.time import Time
from brasileirao.core.entidades.partida import Partida

class TestPartida(unittest.TestCase):
    def test_finalizar_atualiza_pontos_e_saldo(self):
        time_casa = Time('Casa', 'C', 1900, 'Cidade C', 'Estadio C')
        time_vis = Time('Vis', 'V', 1900, 'Cidade V', 'Estadio V')
        partida = Partida(time_casa, time_vis, 1, datetime(2023, 1, 1))
        partida.placar_casa = 2
        partida.placar_visitante = 1
        partida.finalizar()
        self.assertTrue(partida.concluida)
        self.assertEqual(time_casa.pontos, 3)
        self.assertEqual(time_vis.pontos, 0)
        self.assertEqual(time_casa.saldo_gols, 1)
        self.assertEqual(time_vis.saldo_gols, -1)

if __name__ == '__main__':
    unittest.main()
