import tkinter as tk
from ..widgets import TecnicosPopup
from brasileirao.data.times_db import TimesDB
from brasileirao.core.entidades.time import Time
from brasileirao.core.entidades.tecnico import Tecnico
from brasileirao.core.enums.estilo_tatico import EstiloTatico

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
    def __init__(self, master, voltar_cb):
        super().__init__(master)
        self.voltar_cb = voltar_cb
        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self, text="Jogos do Dia", font=HEADER_FONT).pack(pady=5)
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True)
        sb = tk.Scrollbar(frame)
        sb.pack(side="right", fill="y")
        self.lista = tk.Listbox(frame, font=LIST_FONT)
        self.lista.pack(side="left", fill="both", expand=True)
        self.lista.config(yscrollcommand=sb.set)
        sb.config(command=self.lista.yview)

        for i in range(1, 21):
            self.lista.insert("end", f"Time A {i} x Time B {i} - 0 x 0")

        btns = tk.Frame(self)
        btns.pack(pady=5)
        tk.Button(btns, text="Simular", font=BUTTON_FONT, width=18).pack(side="left", padx=5)
        tk.Button(btns, text="Pular para Resultado", font=BUTTON_FONT, width=18).pack(side="left", padx=5)
        tk.Button(btns, text="Avançar", font=BUTTON_FONT, width=18, command=self.voltar_cb).pack(side="left", padx=5)

class SimulacaoFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.times = self._criar_times()
        self.tab_frame = TabelaFrame(self)
        self.rodada_frame = RodadaFrame(self, self.mostrar_tabela)
        self.btn_proxima = tk.Button(self, text="Próxima Rodada", font=BUTTON_FONT, width=18, command=self.mostrar_rodada)
        self.btn_tecnicos = tk.Button(self, text="Ver Técnicos", font=BUTTON_FONT, width=18, command=self.mostrar_tecnicos)
        self.mostrar_tabela()

    def _criar_times(self):
        times = []
        for nome in TimesDB.TIMES_BRASILEIRO_A:
            time = Time(nome, nome, 1900, "Cidade", "Estadio")
            tecnico = Tecnico(f"Técnico {nome}", 50, "Brasil")
            tecnico.estilo_tatico = EstiloTatico.BALANCEADO
            tecnico.time = time
            time.tecnico = tecnico
            times.append(time)
        return times

    def mostrar_tecnicos(self):
        TecnicosPopup(self, self.times)

    def mostrar_tabela(self):
        self.rodada_frame.pack_forget()
        self.tab_frame.pack(fill="both", expand=True)
        self.btn_proxima.pack(pady=5)
        self.btn_tecnicos.pack(pady=5)

    def mostrar_rodada(self):
        self.tab_frame.pack_forget()
        self.btn_proxima.pack_forget()
        self.btn_tecnicos.pack_forget()
        self.rodada_frame.pack(fill="both", expand=True)
