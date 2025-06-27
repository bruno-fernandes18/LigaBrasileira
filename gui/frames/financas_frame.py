"""Frame para exibir informações financeiras do time."""

import tkinter as tk


class FinancasFrame(tk.Frame):
    """Mostra orçamento e despesas salariais."""

    def __init__(self, master: tk.Misc, time) -> None:
        super().__init__(master)
        self.time = time
        tk.Label(self, text="Orçamento: R$ {:,.0f}".format(time.orcamento)).pack(anchor="w")
        tk.Label(self, text="Despesas salariais semanais: R$ {:,.0f}".format(time.despesas_salariais)).pack(anchor="w")
