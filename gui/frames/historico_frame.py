"""Frame de histórico."""

import tkinter as tk

class HistoricoFrame(tk.Frame):
    """Mostra histórico de temporadas."""

    def __init__(self, master: tk.Misc, historico) -> None:
        super().__init__(master)
        for temp in historico.temporadas:
            tk.Label(self, text=str(temp.ano)).pack(anchor='w')
