import tkinter as tk

class TabelaFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self, text="Classificação Série A").pack()
        self.lista = tk.Listbox(self)
        for i in range(1, 5):
            self.lista.insert('end', f"Time {i} - {i*3} pts")
        self.lista.pack(fill='both', expand=True)

class RodadaFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self, text="Jogos do Dia").pack()
        self.lista = tk.Listbox(self)
        for i in range(1, 6):
            self.lista.insert('end', f"Time A {i} x Time B {i} - 0x0")
        self.lista.pack(fill='both', expand=True)

class SimulacaoFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.tab_frame = TabelaFrame(self)
        self.rodada_frame = RodadaFrame(self)
        self.tab_frame.pack(side='left', fill='both', expand=True)
        self.rodada_frame.pack(side='right', fill='both', expand=True)
