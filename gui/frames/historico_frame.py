"""Janela que apresenta o histórico de temporadas salvas."""

import tkinter as tk

class HistoricoFrame(tk.Frame):
    """Mostra histórico de temporadas."""

    def __init__(self, master: tk.Misc, historico) -> None:
        """Constroi o frame.

        Args:
            master: Widget pai.
            historico: Instância de :class:`Historico` contendo temporadas.
        """
        super().__init__(master)
        for temp in historico.temporadas:
            tk.Label(self, text=str(temp.ano)).pack(anchor='w')
