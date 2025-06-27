"""Entidade Copa."""

from datetime import timedelta
from .competicao import Competicao
from .partida import Partida

class Copa(Competicao):
    """Competição eliminatória."""

    def gerar_calendario(self) -> None:
        self.partidas.clear()
        if len(self.times) < 2:
            return
        rodada = 1
        times = list(self.times)
        while len(times) > 1:
            nova_rodada = []
            for i in range(0, len(times), 2):
                casa = times[i]
                visitante = times[i + 1]
                data_base = (
                    self.calendario.partidas[-1].data + timedelta(days=3)
                    if self.calendario.partidas
                    else self.calendario.data_inicio
                )
                partida = Partida(casa, visitante, rodada, data_base)
                self.calendario.adicionar_partida(partida)
                self.partidas.append(partida)
                nova_rodada.append(partida)
            times = [p.time_casa for p in nova_rodada]
            rodada += 1
        self.calendario.verificar_temporada(self.temporada)
        self.calendario.verificar_espacamento_times(self.times)
        self.calendario.verificar_distribuicao_mensal()
