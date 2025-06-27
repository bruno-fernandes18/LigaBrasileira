"""Entidade Liga."""

from .competicao import Competicao
from .partida import Partida

class Liga(Competicao):
    """Liga em formato de pontos corridos."""

    def gerar_calendario(self) -> None:
        super().gerar_calendario()
        self.classificacao = self.times[:]

    def _aplicar_resultado(self, partida: Partida) -> None:
        """Atualiza pontuação e saldo de gols dos times."""
        casa = partida.time_casa
        visitante = partida.time_visitante
        casa.saldo_gols += partida.placar_casa - partida.placar_visitante
        visitante.saldo_gols += partida.placar_visitante - partida.placar_casa

        if partida.placar_casa > partida.placar_visitante:
            casa.pontos += 3
        elif partida.placar_casa < partida.placar_visitante:
            visitante.pontos += 3
        else:
            casa.pontos += 1
            visitante.pontos += 1

    def simular_rodada(self, rodada: int) -> None:
        """Simula as partidas de uma rodada e atualiza a classificação."""
        for partida in self.partidas:
            if partida.rodada == rodada and not partida.concluida:
                partida.simular()
                self._aplicar_resultado(partida)
        self.classificacao.sort(key=lambda t: (t.pontos, t.saldo_gols), reverse=True)
