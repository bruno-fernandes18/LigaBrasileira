"""Sistema de salvamento simples."""

import pickle

class SaveSystem:
    """Gerencia serialização de objetos."""

    @staticmethod
    def salvar(path: str, objeto) -> None:
        with open(path, 'wb') as f:
            pickle.dump(objeto, f)

    @staticmethod
    def carregar(path: str):
        with open(path, 'rb') as f:
            return pickle.load(f)
