"""Ponto de entrada da aplicação."""

import tkinter as tk
from gui.frames.main_menu_frame import MainMenuFrame
from gui.frames.manager_frame import ManagerFrame
from core.entities.time import Time
from simulation.competition.liga_brasileira import LigaBrasileira
from simulation.manager.modo_manager import ModoPlayer

class App(tk.Tk):
    """Janela principal."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Liga Brasileira")

        # Liga de testes com alguns times fictícios
        self.liga = LigaBrasileira("Liga Teste", 2023)
        self.liga.times = [
            Time("Time A", "A", 1900, "Cidade A", "Estádio A"),
            Time("Time B", "B", 1900, "Cidade B", "Estádio B"),
            Time("Time C", "C", 1900, "Cidade C", "Estádio C"),
        ]
        for t in self.liga.times:
            t.liga = self.liga
        self.liga.gerar_calendario()

        # Frame atual da aplicação
        self.frame = MainMenuFrame(self, self)
        self.frame.pack(fill="both", expand=True)

    def iniciar_manager(self) -> None:
        """Entra no modo manager."""
        # Destrói o frame atual (menu principal)
        self.frame.destroy()

        # Jogador controlará o primeiro time da liga
        time_escolhido = self.liga.times[0]
        self.manager = ModoPlayer(time_escolhido)

        # Exibe a tela de gerenciamento
        self.frame = ManagerFrame(self, self.manager)
        self.frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    App().mainloop()
