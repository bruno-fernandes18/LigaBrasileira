"""Componente textual de representação de partidas."""

import tkinter as tk

class PartidaWidget(tk.Frame):
    """Widget simples de partida."""

    def __init__(self, master: tk.Misc, partida) -> None:
        """Exibe os times envolvidos em ``partida``."""
        super().__init__(master)
        texto = f"{partida.time_casa.nome} x {partida.time_visitante.nome}"
        tk.Label(self, text=texto).pack()
