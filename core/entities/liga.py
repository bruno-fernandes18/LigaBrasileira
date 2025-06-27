"""Entidade Liga."""

from .competicao import Competicao
from .partida import Partida

class Liga(Competicao):
    """Liga em formato de pontos corridos."""

    def gerar_calendario(self) -> None:
        for time in self.times:
            time.liga = self
        super().gerar_calendario()
        self.classificacao = self.times[:]

    def _aplicar_resultado(self, partida: Partida) -> None:
        """Atualiza pontuação e saldo de gols usando a partida."""
        partida.aplicar_resultado()

    def simular_rodada(self, rodada: int) -> None:
        """Simula as partidas de uma rodada e atualiza a classificação."""
        for partida in self.partidas:
            if partida.rodada == rodada and not partida.concluida:
                partida.simular()
                self._aplicar_resultado(partida)
        self.classificacao.sort(key=lambda t: (t.pontos, t.saldo_gols), reverse=True)
