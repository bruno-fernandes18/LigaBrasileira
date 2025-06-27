import tkinter as tk
from .simulacao_frame import SimulacaoFrame


HEADER_FONT = ("Helvetica", 24, "bold")
BUTTON_FONT = ("Helvetica", 14)

class MenuFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self, text="Liga Brasileira", font=HEADER_FONT).pack(pady=20)

        texts = [
            ("Iniciar Simulação", self.iniciar),
            ("Jogar com Técnico", None),
            ("Configurações", None),
            ("Sair", self.master.quit),
        ]

        width = max(len(t[0]) for t in texts) + 2
        for text, cmd in texts:
            tk.Button(self, text=text, width=width, font=BUTTON_FONT, command=cmd).pack(pady=5)

        tk.Button(
            self,
            text="Login/Registro",
            font=("Helvetica", 12),
            command=self.mostrar_login,
        ).pack(side="bottom", anchor="e", padx=10, pady=10)

    def iniciar(self):
        self.pack_forget()
        SimulacaoFrame(self.master).pack(fill='both', expand=True)

    def mostrar_login(self):
        popup = tk.Toplevel(self)
        popup.title("Login")
        tk.Label(popup, text="Usuário:").pack()
        tk.Entry(popup).pack()
        tk.Label(popup, text="Senha:").pack()
        tk.Entry(popup, show='*').pack()
        tk.Button(popup, text="Registrar", command=popup.destroy).pack(pady=5)
