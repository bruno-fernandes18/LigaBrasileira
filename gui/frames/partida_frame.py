"""Frame de partida."""

import tkinter as tk
from ..widgets.partida_widget import PartidaWidget


class _Feed(tk.Text):
    """Text widget para exibir eventos."""

    def __init__(self, master: tk.Misc, partida) -> None:
        super().__init__(master, height=10, state="disabled")
        self.partida = partida
        self._atualizar()

    def _atualizar(self) -> None:
        self.config(state="normal")
        self.delete("1.0", tk.END)
        self.insert("end", "\n".join(self.partida.eventos))
        self.config(state="disabled")
        self.after(500, self._atualizar)

class PartidaFrame(tk.Frame):
    """Exibe uma partida."""

    def __init__(self, master: tk.Misc, partida) -> None:
        super().__init__(master)
        PartidaWidget(self, partida).pack()
        _Feed(self, partida).pack(fill="both", expand=True)
