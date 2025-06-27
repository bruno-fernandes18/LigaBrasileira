"""Ponto de entrada da aplicação GUI."""

import logging
import importlib
import tkinter as tk
from importlib import metadata

from tkinter import messagebox

from brasileirao.gui import initializer


logging.basicConfig(level=logging.INFO)


def check_dependencies() -> None:
    """Verifica a presença de dependências essenciais.

    Em caso de dependências ausentes, uma janela de alerta é exibida
    para o usuário em vez de lançar ``ImportError``.
    """

    required = {"PIL", "numpy", "pandas"}
    missing = {name for name in required if importlib.util.find_spec(name) is None}
    if missing:
        messagebox.showerror(
            "Dependências ausentes",
            f"Faltam módulos: {', '.join(sorted(missing))}",
        )

class MainWindow(tk.Tk):
    """Janela principal da aplicação."""

    def __init__(self) -> None:
        super().__init__()
        initializer.start(self)

    def run(self) -> None:
        """Inicia o loop principal da aplicação."""

        self.mainloop()

if __name__ == "__main__":
    check_dependencies()
    MainWindow().run()
