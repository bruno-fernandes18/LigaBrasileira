import datetime
from brasileirao.core.entidades.competicao import Competicao
from brasileirao.core.entidades.time import Time
from brasileirao.data.times_db import TimesDB


class AppController:
    """Gerencia os dados principais da aplicação."""

    def __init__(self) -> None:
        temporada = datetime.datetime.now().year
        self.campeonato = Competicao("Brasileirão", temporada)
        for nome in TimesDB.TIMES_BRASILEIRO_A:
            self.campeonato.adicionar_time(
                Time(nome, nome, 1900, "Cidade", f"Estádio {nome}")
            )
        self.campeonato.gerar_calendario()
        self.campeonato.atualizar_classificacao()
