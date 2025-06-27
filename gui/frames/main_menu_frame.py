"""Tela inicial apresentada ao usuário."""

import tkinter as tk

class MainMenuFrame(tk.Frame):
    """Menu principal da aplicação."""

    def __init__(self, master: tk.Misc, app) -> None:
        """Cria o menu.

        Args:
            master: Container tkinter.
            app: Instância principal usada para acionar ações.
        """
        super().__init__(master)
        tk.Button(self, text="Iniciar", command=app.iniciar_manager).pack(pady=10)
