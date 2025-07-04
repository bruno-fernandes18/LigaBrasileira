"""Componente que lista a posição dos times."""

import tkinter as tk

class ClassificacaoWidget(tk.Frame):
    """Widget de classificação simples."""

    def __init__(self, master: tk.Misc, classificacao) -> None:
        """Cria labels mostrando a ordem dos times."""
        super().__init__(master)
        for i, time in enumerate(classificacao, 1):
            tk.Label(self, text=f"{i} - {time.nome}").pack(anchor='w')
