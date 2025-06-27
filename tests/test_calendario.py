import os
import sys
import unittest
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from brasileirao.core.entidades.time import Time
from brasileirao.core.entidades.partida import Partida
from brasileirao.core.entidades.calendario import Calendario

class TestCalendario(unittest.TestCase):
    def test_adicionar_partida_ajusta_data(self):
        time_a = Time('Time A', 'A', 1900, 'Cidade A', 'Estadio A')
        time_b = Time('Time B', 'B', 1900, 'Cidade B', 'Estadio B')
        cal = Calendario()
        primeira_data = datetime(2023, 1, 1)
        segunda_data = datetime(2023, 1, 2)
        p1 = Partida(time_a, time_b, 1, primeira_data)
        p2 = Partida(time_a, time_b, 2, segunda_data)
        cal.adicionar_partida(p1)
        cal.adicionar_partida(p2)
        self.assertGreaterEqual((p2.data - p1.data).days, 3)

if __name__ == '__main__':
    unittest.main()
