import tkinter as tk

HEADER_FONT = ("Helvetica", 18, "bold")
LIST_FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 14)

class TabelaFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self, text="Classificação Série A", font=HEADER_FONT).pack(pady=5)
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True)
        sb = tk.Scrollbar(frame)
        sb.pack(side="right", fill="y")
        self.lista = tk.Listbox(frame, font=LIST_FONT)
        self.lista.pack(side="left", fill="both", expand=True)
        self.lista.config(yscrollcommand=sb.set)
        sb.config(command=self.lista.yview)

        for i in range(1, 21):
            self.lista.insert("end", f"{i:2d} - Time {i} - {i*3} pts")

class RodadaFrame(tk.Frame):
    """Exibe a lista de partidas de uma rodada."""

    def __init__(self, master, partidas=None, voltar_cb=None):
        super().__init__(master)
        self.voltar_cb = voltar_cb
        self.partidas = partidas or []
        self._criar_widgets()

    def _criar_widgets(self):
        tk.Label(self, text="Jogos do Dia", font=HEADER_FONT).pack(pady=5)
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True)
        sb = tk.Scrollbar(frame)
        sb.pack(side="right", fill="y")
        self.lista = tk.Listbox(frame, font=LIST_FONT)
        self.lista.pack(side="left", fill="both", expand=True)
        self.lista.config(yscrollcommand=sb.set)
        sb.config(command=self.lista.yview)

        self.atualizar_partidas(self.partidas)

        btns = tk.Frame(self)
        btns.pack(pady=5)
        tk.Button(btns, text="Simular", font=BUTTON_FONT, width=18).pack(
            side="left", padx=5
        )
        tk.Button(btns, text="Pular para Resultado", font=BUTTON_FONT, width=18).pack(
            side="left", padx=5
        )
        if self.voltar_cb:
            tk.Button(
                btns,
                text="Avançar",
                font=BUTTON_FONT,
                width=18,
                command=self.voltar_cb,
            ).pack(side="left", padx=5)

    def atualizar_partidas(self, partidas):
        """Atualiza a listbox com objetos de :class:`Partida`."""
        self.partidas = partidas
        self.lista.delete(0, tk.END)
        for p in self.partidas:
            try:
                desc = (
                    f"{p.time_casa.apelido} x {p.time_visitante.apelido}"
                    f" - {p.placar_casa} x {p.placar_visitante}"
                )
            except AttributeError:
                desc = str(p)
            self.lista.insert("end", desc)

class SimulacaoFrame(tk.Frame):
    """Frame principal da simulação."""

    def __init__(self, master, partidas=None):
        super().__init__(master)
        self.partidas = partidas or []
        self.tab_frame = TabelaFrame(self)
        self.rodada_frame = RodadaFrame(
            self, partidas=self.partidas, voltar_cb=self.mostrar_tabela
        )
        self.btn_proxima = tk.Button(
            self,
            text="Próxima Rodada",
            font=BUTTON_FONT,
            width=18,
            command=self.mostrar_rodada,
        )
        self.mostrar_tabela()

    def mostrar_tabela(self):
        """Exibe a tabela de classificação."""
        self.rodada_frame.pack_forget()
        self.tab_frame.pack(fill="both", expand=True)
        self.btn_proxima.pack(pady=5)

    def mostrar_rodada(self):
        """Mostra as partidas da rodada atual sem recriar widgets."""
        self.tab_frame.pack_forget()
        self.btn_proxima.pack_forget()
        self.rodada_frame.atualizar_partidas(self.partidas)
        self.rodada_frame.pack(fill="both", expand=True)

