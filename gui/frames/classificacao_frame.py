"""Frame de classificação."""

import tkinter as tk
from ..widgets.classificacao_widget import ClassificacaoWidget

class ClassificacaoFrame(tk.Frame):
    """Exibe a classificação de uma competição."""

    def __init__(self, master: tk.Misc, classificacao) -> None:
        super().__init__(master)
        ClassificacaoWidget(self, classificacao).pack()
