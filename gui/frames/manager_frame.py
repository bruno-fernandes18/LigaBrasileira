"""Tela utilizada durante o gerenciamento do time."""

import tkinter as tk
from ..widgets.classificacao_widget import ClassificacaoWidget

class ManagerFrame(tk.Frame):
    """Tela principal do modo manager."""

    def __init__(self, master: tk.Misc, manager) -> None:
        """Constrói a interface de gerenciamento.

        Args:
            master: Container pai.
            manager: Objeto responsável pelo modo de jogo.
        """
        super().__init__(master)
        self.manager = manager
        liga = getattr(manager.time, "liga", None)
        classificacao = liga.classificacao if liga else []
        ClassificacaoWidget(self, classificacao).pack()
