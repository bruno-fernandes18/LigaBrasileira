import tkinter as tk
from .simulacao_frame import SimulacaoFrame

class MenuFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self, text="Liga Brasileira", font=("Arial", 20)).pack(pady=10)
        btn_sim = tk.Button(self, text="Iniciar Simulação", command=self.iniciar)
        btn_manager = tk.Button(self, text="Jogar com Técnico")
        btn_cfg = tk.Button(self, text="Configurações")
        btn_sair = tk.Button(self, text="Sair", command=self.master.quit)
        btn_login = tk.Button(self, text="Login/Registro", command=self.mostrar_login)
        btn_sim.pack(pady=2)
        btn_manager.pack(pady=2)
        btn_cfg.pack(pady=2)
        btn_sair.pack(pady=2)
        btn_login.pack(side="bottom", anchor="se")

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
