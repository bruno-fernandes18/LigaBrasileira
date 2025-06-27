"""Gerenciamento de calendário."""

from datetime import date, timedelta
from .partida import Partida

class Calendario:
    """Armazena partidas e calcula datas disponíveis."""

    def __init__(self) -> None:
        self.partidas: list[Partida] = []
        self.rodada_atual = 1
        self.data_inicio: date = date.today()

    def adicionar_partida(self, partida: Partida) -> None:
        """Adiciona partida mantendo espaçamento mínimo."""
        if self.partidas and (partida.data - self.partidas[-1].data).days < 3:
            partida.data = self.partidas[-1].data + timedelta(days=3)
        self.partidas.append(partida)

    def proxima_data_disponivel(self, data_inicio: date) -> date:
        """Retorna a próxima data livre a partir de ``data_inicio``."""
        data = data_inicio
        if self.partidas:
            while any(abs(((p.data.date() if hasattr(p.data, 'date') else p.data) - data).days) < 3 for p in self.partidas):
                data += timedelta(days=1)
        return data
