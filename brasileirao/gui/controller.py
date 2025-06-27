import datetime
from brasileirao.core.entidades.competicao import Competicao
from brasileirao.core.entidades.time import Time
from brasileirao.data.times_db import TimesDB
from brasileirao.persistence.history_manager import HistoryManager


class AppController:
    """Gerencia os dados principais da aplicação."""

    def __init__(self) -> None:
        temporada = datetime.datetime.now().year
        self.historico = HistoryManager()
        self.campeonato = Competicao("Brasileirão", temporada)
        self.times = []
        self.jogadores = []
        for nome in TimesDB.TIMES_BRASILEIRO_A:
            time = Time(nome, nome, 1900, "Cidade", f"Estádio {nome}")
            self.campeonato.adicionar_time(time)
            self.times.append(time)
        self.campeonato.gerar_calendario()
        self.campeonato.atualizar_classificacao()

    def carregar_dados(self) -> None:
        """Ponto de extensão para carregar dados de arquivos."""
        pass

    def salvar_estado(self) -> dict:
        """Retorna dicionário simples representando o estado atual."""

        return {
            "temporada": self.campeonato.temporada,
            "times": [t.nome for t in self.times],
            "historico": self.historico.historico.temporadas,
        }
