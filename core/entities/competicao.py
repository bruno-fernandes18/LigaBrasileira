"""Entidade Competicao."""

from __future__ import annotations
from typing import List
from datetime import datetime, date
from .time import Time
from .partida import Partida
from .calendario import Calendario

class Competicao:
    """Gerencia uma competição entre times."""

    def __init__(self, nome: str, temporada: int, dependente_de: 'Competicao | None' = None) -> None:
        self.nome = nome
        self.temporada = temporada
        self.times: List[Time] = []
        self.partidas: List[Partida] = []
        self.classificacao: List[Time] = []
        self.dependente_de = dependente_de
        self.calendario = Calendario()

    def gerar_calendario(self) -> None:
        """Gera calendário básico ida e volta."""
        self.partidas.clear()
        if len(self.times) < 2:
            return
        data = date(self.temporada, 1, 1)
        rodada = 1
        for i, casa in enumerate(self.times):
            for visitante in self.times[i+1:]:
                p1 = Partida(casa, visitante, rodada, datetime.combine(data, datetime.min.time()))
                self.calendario.adicionar_partida(p1)
                self.partidas.append(p1)
                data = self.calendario.proxima_data_disponivel(data)
                rodada += 1
                p2 = Partida(visitante, casa, rodada, datetime.combine(data, datetime.min.time()))
                self.calendario.adicionar_partida(p2)
                self.partidas.append(p2)
                data = self.calendario.proxima_data_disponivel(data)
                rodada += 1

    def simular_rodada(self, rodada: int) -> None:
        """Simula as partidas de uma rodada."""
        for partida in self.partidas:
            if partida.rodada == rodada and not partida.concluida:
                partida.simular()
