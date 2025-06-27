"""Histórico de temporadas."""

class TemporadaHistorico:
    """Registra informações de uma temporada."""

    def __init__(self, ano: int) -> None:
        self.ano = ano
        self.campeonatos: dict[str, str] = {}
        self.artilheiros: dict[str, str] = {}
        self.classificacao: list[str] = []
        self.trofeus_por_time: dict[str, list[str]] = {}

class Historico:
    """Coleção de temporadas."""

    def __init__(self) -> None:
        self.temporadas: list[TemporadaHistorico] = []

    def adicionar_temporada(self, temporada: TemporadaHistorico) -> None:
        self.temporadas.append(temporada)

    def _obter_ou_criar(self, ano: int) -> TemporadaHistorico:
        for temp in self.temporadas:
            if temp.ano == ano:
                return temp
        novo = TemporadaHistorico(ano)
        self.temporadas.append(novo)
        return novo

    def registrar_campeonato(self, ano: int, nome: str, campeao: str) -> None:
        temporada = self._obter_ou_criar(ano)
        temporada.campeonatos[nome] = campeao
        temporada.trofeus_por_time.setdefault(campeao, []).append(nome)

    def registrar_artilheiro(self, ano: int, competicao: str, jogador: str) -> None:
        temporada = self._obter_ou_criar(ano)
        temporada.artilheiros[competicao] = jogador

    def registrar_classificacao(self, ano: int, classificacao: list[str]) -> None:
        temporada = self._obter_ou_criar(ano)
        temporada.classificacao = classificacao
