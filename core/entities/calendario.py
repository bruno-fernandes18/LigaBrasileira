"""Gerenciamento de calendário."""

from datetime import date, timedelta
from .partida import Partida
from .time import Time

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

    def verificar_temporada(self, temporada: int) -> bool:
        """Verifica se todas as partidas estão dentro da temporada indicada."""
        inicio = date(temporada, 1, 1)
        fim = date(temporada, 12, 31)
        for partida in self.partidas:
            data = partida.data.date() if hasattr(partida.data, "date") else partida.data
            if not (inicio <= data <= fim):
                return False
        return True

    def verificar_espacamento_times(self, times: list[Time], dias: int = 3) -> bool:
        """Garante espaçamento mínimo de ``dias`` para cada time."""
        for time in times:
            jogos = sorted(
                [p.data for p in self.partidas if p.time_casa is time or p.time_visitante is time]
            )
            for d1, d2 in zip(jogos, jogos[1:]):
                if (d2 - d1).days < dias:
                    return False
        return True

    def verificar_distribuicao_mensal(self) -> bool:
        """Verifica se há distribuição razoável de partidas entre os meses."""
        total = len(self.partidas)
        if total < 10:
            return True
        contagem: dict[int, int] = {}
        for partida in self.partidas:
            mes = partida.data.month
            contagem[mes] = contagem.get(mes, 0) + 1
        if len(contagem) <= 1:
            return False
        media = total / len(contagem)
        return all(abs(c - media) <= 5 for c in contagem.values())
