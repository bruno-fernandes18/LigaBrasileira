"""Componente de exibição para dados de um time."""

import tkinter as tk

class TimeWidget(tk.Frame):
    """Widget simples de time."""

    def __init__(self, master: tk.Misc, time) -> None:
        """Apresenta o nome do ``time``."""
        super().__init__(master)
        tk.Label(self, text=getattr(time, 'nome', 'Time')).pack()
