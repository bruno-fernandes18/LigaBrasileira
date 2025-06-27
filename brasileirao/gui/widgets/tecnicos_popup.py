import tkinter as tk

HEADER_FONT = ("Helvetica", 18, "bold")
LIST_FONT = ("Helvetica", 12)

class TecnicosPopup(tk.Toplevel):
    """Janela popup exibindo informacoes dos tecnicos."""

    def __init__(self, master, times):
        super().__init__(master)
        self.title("Tecnicos")
        self.geometry("500x400")
        self.resizable(False, False)
        tk.Label(self, text="Tecnicos dos Times", font=HEADER_FONT).pack(pady=5)
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True, padx=10, pady=5)
        sb = tk.Scrollbar(frame)
        sb.pack(side="right", fill="y")
        self.lista = tk.Listbox(frame, font=LIST_FONT)
        self.lista.pack(side="left", fill="both", expand=True)
        self.lista.config(yscrollcommand=sb.set)
        sb.config(command=self.lista.yview)
        for time in times:
            tecnico = getattr(time, "tecnico", None)
            if tecnico is None:
                continue
            estilo = getattr(tecnico.estilo_tatico, "name", "").replace("_", " ").title()
            texto = (
                f"{time.nome} - {tecnico.nome} - {tecnico.idade} anos - "
                f"{tecnico.nacionalidade} - {estilo}"
            )
            self.lista.insert("end", texto)
        tk.Button(self, text="Fechar", command=self.destroy).pack(pady=5)
