"""Rotinas de serialização usando *pickle*.

Este módulo disponibiliza uma classe utilitária para salvar e carregar
objetos Python de forma simples. Os métodos são estáticos para facilitar
o uso em diferentes partes da aplicação.
"""

import pickle

class SaveSystem:
    """Gerencia a persistência de objetos."""

    @staticmethod
    def salvar(path: str, objeto) -> None:
        """Serializa ``objeto`` no caminho indicado.

        Args:
            path: Arquivo de destino.
            objeto: Instância Python serializável via ``pickle``.
        """
        with open(path, 'wb') as f:
            pickle.dump(objeto, f)

    @staticmethod
    def carregar(path: str):
        """Deserializa um objeto a partir de ``path``.

        Args:
            path: Arquivo que contém os dados serializados.

        Returns:
            Objeto carregado do arquivo.
        """
        with open(path, 'rb') as f:
            return pickle.load(f)
