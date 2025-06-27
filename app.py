"""Ponto de entrada da aplicação."""

import tkinter as tk
from gui.frames.main_menu_frame import MainMenuFrame

class App(tk.Tk):
    """Janela principal."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Liga Brasileira")
        MainMenuFrame(self, self).pack(fill="both", expand=True)

    def iniciar_manager(self) -> None:
        pass  # placeholder para inicializar modo manager

if __name__ == "__main__":
    App().mainloop()
