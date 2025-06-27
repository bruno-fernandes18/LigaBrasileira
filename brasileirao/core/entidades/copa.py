from typing import Optional
from .partida import Partida
from .competicao import Competicao

class Copa(Competicao):
    """Competição eliminatória dependente de outra competição."""

    def __init__(self, nome: str, temporada: int, dependente_de: Optional[Competicao] = None):
        super().__init__(nome, temporada)
        self.dependente_de = dependente_de
        self.chaves = []

    def gerar_calendario(self):
        if not self.times:
            return
        from datetime import timedelta
        self.partidas.clear()
        rodada = 1
        data = self.calendario.data_inicio
        times = list(self.times)
        while len(times) > 1:
            nova_rodada = []
            for i in range(0, len(times), 2):
                casa = times[i]
                visitante = times[i + 1]
                partida = Partida(casa, visitante, rodada, data)
                self.calendario.adicionar_partida(partida)
                self.partidas.append(partida)
                nova_rodada.append(partida)
            data += timedelta(days=7)
            rodada += 1
            times = [p.time_casa if p.placar_casa > p.placar_visitante else p.time_visitante for p in nova_rodada]
