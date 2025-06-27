"""Janela para visualização de uma partida."""

import tkinter as tk
from ..widgets.partida_widget import PartidaWidget

class PartidaFrame(tk.Frame):
    """Exibe uma partida."""

    def __init__(self, master: tk.Misc, partida) -> None:
        """Inicializa o frame.

        Args:
            master: Widget pai na hierarquia tkinter.
            partida: Objeto de partida a ser exibido.
        """
        super().__init__(master)
        PartidaWidget(self, partida).pack()
