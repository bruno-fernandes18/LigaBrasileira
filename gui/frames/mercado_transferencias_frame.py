"""Frame para mostrar jogadores disponíveis no mercado de transferências."""

import tkinter as tk
from ..widgets.jogador_widget import JogadorWidget


class MercadoTransferenciasFrame(tk.Frame):
    """Lista jogadores de outros times."""

    def __init__(self, master: tk.Misc, jogadores) -> None:
        super().__init__(master)
        for j in jogadores:
            JogadorWidget(self, j).pack(anchor="w")
