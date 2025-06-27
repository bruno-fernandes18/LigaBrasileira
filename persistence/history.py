"""Estruturas para armazenar estatísticas de temporadas."""

class TemporadaHistorico:
    """Registra informações de uma temporada."""

    def __init__(self, ano: int) -> None:
        """Cria um novo registro.

        Args:
            ano: Ano da temporada.
        """
        self.ano = ano
        self.campeonatos: dict[str, str] = {}
        self.artilheiros: dict[str, str] = {}
        self.classificacao: list[str] = []
        self.trofeus_por_time: dict[str, list[str]] = {}

class Historico:
    """Coleção de temporadas."""

    def __init__(self) -> None:
        """Inicializa o histórico vazio."""
        self.temporadas: list[TemporadaHistorico] = []

    def adicionar_temporada(self, temporada: TemporadaHistorico) -> None:
        """Adiciona uma temporada ao histórico."""
        self.temporadas.append(temporada)

    def _obter_ou_criar(self, ano: int) -> TemporadaHistorico:
        """Retorna o registro de ``ano`` ou cria um novo."""
        for temp in self.temporadas:
            if temp.ano == ano:
                return temp
        novo = TemporadaHistorico(ano)
        self.temporadas.append(novo)
        return novo

    def registrar_campeonato(self, ano: int, nome: str, campeao: str) -> None:
        """Grava o campeão de uma competição."""
        temporada = self._obter_ou_criar(ano)
        temporada.campeonatos[nome] = campeao
        temporada.trofeus_por_time.setdefault(campeao, []).append(nome)

    def registrar_artilheiro(self, ano: int, competicao: str, jogador: str) -> None:
        """Registra o artilheiro de ``competicao`` em ``ano``."""
        temporada = self._obter_ou_criar(ano)
        temporada.artilheiros[competicao] = jogador

    def registrar_classificacao(self, ano: int, classificacao: list[str]) -> None:
        """Armazena a classificação final de ``ano``."""
        temporada = self._obter_ou_criar(ano)
        temporada.classificacao = classificacao
