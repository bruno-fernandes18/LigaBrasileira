from .competicao import Competicao

class Liga(Competicao):
    """Competição em formato de pontos corridos."""

    def gerar_calendario(self):
        super().gerar_calendario()
        self.calendario.partidas = self.partidas
        self.atualizar_classificacao()
