"""Componente para renderização de informações de jogadores."""

import tkinter as tk

class JogadorWidget(tk.Frame):
    """Widget simples de jogador."""

    def __init__(self, master: tk.Misc, jogador) -> None:
        """Mostra o nome do ``jogador``."""
        super().__init__(master)
        tk.Label(self, text=getattr(jogador, 'nome', 'Jogador')).pack()
