"""Frame principal do menu."""

import tkinter as tk

class MainMenuFrame(tk.Frame):
    """Menu principal da aplicação."""

    def __init__(self, master: tk.Misc, app) -> None:
        super().__init__(master)
        tk.Button(self, text="Iniciar", command=app.iniciar_manager).pack(pady=10)
