"""Entidade Liga."""

from .competicao import Competicao
from .partida import Partida
from .jogador import Jogador

class Liga(Competicao):
    """Liga em formato de pontos corridos."""

    def __init__(self, nome: str, temporada: int, dependente_de: Competicao | None = None) -> None:
        super().__init__(nome, temporada, dependente_de)
        self.artilharia: dict[Jogador, int] = {}
        self.assistencias: dict[Jogador, int] = {}

    def gerar_calendario(self) -> None:
        for time in self.times:
            time.liga = self
        super().gerar_calendario()
        self.classificacao = self.times[:]
        self.calendario.verificar_temporada(self.temporada)
        self.calendario.verificar_espacamento_times(self.times)
        self.calendario.verificar_distribuicao_mensal()

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
