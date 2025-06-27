"""Widget para exibir jogador."""

import tkinter as tk

class JogadorWidget(tk.Frame):
    """Widget simples de jogador."""

    def __init__(self, master: tk.Misc, jogador) -> None:
        super().__init__(master)
        tk.Label(self, text=getattr(jogador, 'nome', 'Jogador')).pack()
