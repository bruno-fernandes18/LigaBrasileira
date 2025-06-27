import tkinter as tk
from datetime import datetime

from ..widgets import TecnicosPopup
from brasileirao.core.entidades.competicao import Competicao
from ..controller import AppController

HEADER_FONT = ("Helvetica", 18, "bold")
LIST_FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 14)


class TabelaFrame(tk.Frame):
    """Exibe a classificação de uma competição."""

    def __init__(self, master: tk.Misc, competicao: Competicao | None = None):
        super().__init__(master)
        if not competicao:
            competicao = Competicao("Brasileirão", datetime.now().year)
        self.competicao = competicao
        self.lista = None
        self.criar_widgets()

    def criar_widgets(self):
        """Cria widgets da tabela de classificação."""

        tk.Label(self, text="Classificação Série A", font=HEADER_FONT).pack(pady=5)
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True)
        sb = tk.Scrollbar(frame)
        sb.pack(side="right", fill="y")
        self.lista = tk.Listbox(frame, font=LIST_FONT)
        self.lista.pack(side="left", fill="both", expand=True)
        self.lista.config(yscrollcommand=sb.set)
        sb.config(command=self.lista.yview)

    def atualizar(self):
        """Atualiza a tabela com a classificação atual."""

        self.lista.delete(0, tk.END)
        for i, time in enumerate(self.competicao.classificacao, 1):
            self.lista.insert(tk.END, f"{i:2d} - {time.nome} - {time.pontos} pts")


class RodadaFrame(tk.Frame):
    """Exibe a lista de partidas de uma rodada."""

    def __init__(
        self,
        master: tk.Misc,
        competicao: Competicao,
        rodada: int,
        concluir_cb,
    ) -> None:
        super().__init__(master)
        self.competicao = competicao
        self.rodada = rodada
        self.concluir_cb = concluir_cb
        self.lista = None
        self.btn_sim = None
        self._criar_widgets()

    def _criar_widgets(self) -> None:
        tk.Label(self, text=f"Rodada {self.rodada}", font=HEADER_FONT).pack(pady=5)
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True)
        sb = tk.Scrollbar(frame)
        sb.pack(side="right", fill="y")
        self.lista = tk.Listbox(frame, font=LIST_FONT)
        self.lista.pack(side="left", fill="both", expand=True)
        self.lista.config(yscrollcommand=sb.set)
        sb.config(command=self.lista.yview)
        self.atualizar_lista()

        btns = tk.Frame(self)
        btns.pack(pady=5)
        self.btn_sim = tk.Button(btns, text="Simular", font=BUTTON_FONT, width=18, command=self.simular)
        self.btn_sim.pack(side="left", padx=5)
        tk.Button(btns, text="Pular para Resultado", font=BUTTON_FONT, width=18).pack(side="left", padx=5)
        tk.Button(btns, text="Avançar", font=BUTTON_FONT, width=18, command=self.finalizar).pack(side="left", padx=5)

    def atualizar_lista(self):
        """Atualiza a lista de partidas na listbox."""

        self.lista.delete(0, tk.END)
        partidas = [p for p in self.competicao.partidas if p.rodada == self.rodada]
        for p in partidas:
            if p.concluida:
                texto = f"{p.time_casa.nome} {p.placar_casa} x {p.placar_visitante} {p.time_visitante.nome}"
            else:
                texto = f"{p.time_casa.nome} x {p.time_visitante.nome} - {p.data.strftime('%d/%m')}"
            self.lista.insert(tk.END, texto)

    def simular(self):
        """Simula os jogos da rodada atual."""

        self.competicao.simular_rodada(self.rodada)
        self.btn_sim.config(state=tk.DISABLED)
        self.atualizar_lista()
        if hasattr(self.master, "tab_frame"):
            self.master.tab_frame.atualizar()

    def finalizar(self):
        """Encerra a rodada e aciona callback externa."""

        self.concluir_cb()



class SimulacaoFrame(tk.Frame):
    """Frame principal da simulação."""

    def __init__(self, parent: tk.Misc, controller: AppController):
        super().__init__(parent)

        self.controller = controller
        self.competicao = controller.campeonato
        partidas = None

        self.rodada_atual = 1
        self.partidas = partidas or []

        self.tab_frame = TabelaFrame(self, self.competicao)
        self.rodada_frame = RodadaFrame(
            self, self.competicao, self.rodada_atual, self.finalizar_rodada
        )
        self.btn_proxima = tk.Button(
            self, text="Próxima Rodada", font=BUTTON_FONT, width=18, command=self.mostrar_rodada
        )
        self.btn_tecnicos = tk.Button(
            self, text="Ver Técnicos", font=BUTTON_FONT, width=18, command=self.mostrar_tecnicos
        )

        self.mostrar_tabela()

    def mostrar_tecnicos(self):
        """Exibe lista de técnicos em um popup."""

        TecnicosPopup(self, self.competicao.times)

    def mostrar_tabela(self):
        """Exibe a tabela de classificação."""

        self.rodada_frame.pack_forget()
        self.tab_frame.pack(fill="both", expand=True)
        self.btn_proxima.pack(pady=5)
        self.btn_tecnicos.pack(pady=5)
        if self.rodada_atual <= len(self.competicao.partidas) // (
            len(self.competicao.times) // 2
        ):
            self.btn_proxima.pack(pady=5)

    def mostrar_rodada(self):
        """Mostra as partidas da rodada atual sem recriar widgets."""

        self.tab_frame.pack_forget()
        self.btn_proxima.pack_forget()
        self.btn_tecnicos.pack_forget()
        self.rodada_frame.pack_forget()
        self.rodada_frame = RodadaFrame(
            self, self.competicao, self.rodada_atual, self.finalizar_rodada
        )
        self.rodada_frame.pack(fill="both", expand=True)

    def finalizar_rodada(self):
        """Avança para a próxima rodada."""

        self.rodada_atual += 1
        self.mostrar_tabela()
        self.rodada_frame.atualizar_partidas(self.partidas)
        self.rodada_frame.pack(fill="both", expand=True)

