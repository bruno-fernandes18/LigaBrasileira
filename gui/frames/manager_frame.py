"""Frame do modo manager."""

import tkinter as tk
from ..widgets.classificacao_widget import ClassificacaoWidget

class ManagerFrame(tk.Frame):
    """Tela principal do modo manager."""

    def __init__(self, master: tk.Misc, manager) -> None:
        super().__init__(master)
        self.manager = manager
        ClassificacaoWidget(self, manager.time.liga.classificacao).pack()
