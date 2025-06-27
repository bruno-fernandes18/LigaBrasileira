"""Implementação da Liga da Segunda Divisão."""

from datetime import date

from core.entities.liga import Liga
from core.entities.calendario import Calendario
from core.entities.time import Time
from core.data.times_db import TIMES_SERIE_B


class LigaSegundaDivisao(Liga):
    """Liga da Série B do campeonato brasileiro."""

    def __init__(self, nome: str, temporada: int, dependente_de=None) -> None:
        super().__init__(nome, temporada, dependente_de)
        self._popular_times()

    def _popular_times(self) -> None:
        """Cria clubes a partir da lista de times da Série B."""
        self.times = [
            Time(nome, nome[0], 1900, "Cidade", "Estádio") for nome in TIMES_SERIE_B
        ]
        for t in self.times:
            t.liga = self

    def gerar_calendario(self) -> None:
        for time in self.times:
            time.liga = self
        self.calendario = Calendario()
        data = date(self.temporada, 1, 1)
        self.partidas.clear()
        rodada = 1
        for i, casa in enumerate(self.times):
            for visitante in self.times[i + 1 :]:
                partida = self._criar_partida(casa, visitante, rodada, data)
                rodada += 1
                data = self.calendario.proxima_data_disponivel(data)
                partida_volta = self._criar_partida(visitante, casa, rodada, data)
                rodada += 1
                data = self.calendario.proxima_data_disponivel(data)
        self.classificacao = self.times[:]

    def _criar_partida(self, casa, visitante, rodada, data):
        from core.entities.partida import Partida

        partida = Partida(casa, visitante, rodada, data)
        self.calendario.adicionar_partida(partida)
        self.partidas.append(partida)
        return partida
