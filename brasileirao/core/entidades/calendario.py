from datetime import datetime, timedelta

class Calendario:
    def __init__(self):
        self.partidas = []
        self.data_inicio = datetime(2023, 1, 1)
        self.data_fim = datetime(2023, 12, 31)

    def adicionar_partida(self, partida):
        if not self.verificar_disponibilidade_data(partida.data):
            partida.data = self.encontrar_proxima_data_disponivel(partida.data)
        self.partidas.append(partida)
        self.partidas.sort(key=lambda p: p.data)

    def verificar_disponibilidade_data(self, data: datetime) -> bool:
        if data < self.data_inicio or data > self.data_fim:
            return False
        for partida in self.partidas:
            if abs((partida.data - data).days) < 3:
                return False
        return True

    def encontrar_proxima_data_disponivel(self, data: datetime) -> datetime:
        tentativa = data + timedelta(days=3)
        while not self.verificar_disponibilidade_data(tentativa):
            tentativa += timedelta(days=1)
        return tentativa
