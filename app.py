"""Ponto de entrada da aplicação GUI."""

import tkinter as tk
from importlib import metadata

from brasileirao.gui import initializer


def check_dependencies() -> None:
    """Verifica a presença de dependências essenciais."""

    required = {"PIL", "numpy", "pandas"}
    installed = {dist.metadata["Name"] for dist in metadata.distributions()}
    missing = required - installed
    if missing:
        raise ImportError(f"Faltam módulos: {', '.join(sorted(missing))}")

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
