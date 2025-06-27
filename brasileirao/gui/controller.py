import datetime
from brasileirao.core.entidades.competicao import Competicao
from brasileirao.core.entidades.time import Time
from brasileirao.data.times_db import TimesDB
from brasileirao.persistence.history_manager import HistoryManager


class AppController:
    """Gerencia os dados principais da aplicação."""

    def __init__(self) -> None:
        """Inicializa o controlador e cria a estrutura básica do campeonato."""

        temporada = datetime.datetime.now().year
        self.historico = HistoryManager()
        self.campeonato = Competicao("Brasileirão", temporada)
        self.times: list[Time] = []
        self.jogadores = []
        for nome in TimesDB.TIMES_BRASILEIRO_A:
            time = Time(nome, nome, 1900, "Cidade", f"Estádio {nome}")
            self.adicionar_time(time)
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

    def adicionar_time(self, time: Time) -> None:
        """Registra um novo time na competição."""

        self.campeonato.adicionar_time(time)
        self.times.append(time)

    def get_campeonato(self) -> Competicao:
        """Retorna a competição principal gerenciada pelo controlador."""

        return self.campeonato

    def registrar_temporada(self, campeao: str) -> None:
        """Armazena o resultado de uma temporada no histórico."""

        temporada = {
            "ano": self.campeonato.temporada,
            "campeao": campeao,
        }
        self.historico.adicionar_temporada(temporada)
