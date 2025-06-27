"""Implementação da Liga Brasileira."""

from datetime import date
from ...core.entities.liga import Liga
from ...core.entities.calendario import Calendario

class LigaBrasileira(Liga):
    """Liga nacional com calendário semanal."""

    def gerar_calendario(self) -> None:
        self.calendario = Calendario()
        data = date(self.temporada, 1, 1)
        self.partidas.clear()
        rodada = 1
        for i, casa in enumerate(self.times):
            for visitante in self.times[i+1:]:
                partida = self._criar_partida(casa, visitante, rodada, data)
                rodada += 1
                data = self.calendario.proxima_data_disponivel(data)
                partida_volta = self._criar_partida(visitante, casa, rodada, data)
                rodada += 1
                data = self.calendario.proxima_data_disponivel(data)

    def _criar_partida(self, casa, visitante, rodada, data):
        from ...core.entities.partida import Partida
        partida = Partida(casa, visitante, rodada, data)
        self.calendario.adicionar_partida(partida)
        self.partidas.append(partida)
        return partida
