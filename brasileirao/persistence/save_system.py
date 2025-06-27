import os
import pickle

class SaveSystem:
    SAVE_DIR = 'saves'

    @staticmethod
    def salvar_jogo(estado, nome_arquivo='save01.sav'):
        if not os.path.exists(SaveSystem.SAVE_DIR):
            os.makedirs(SaveSystem.SAVE_DIR)
        with open(os.path.join(SaveSystem.SAVE_DIR, nome_arquivo), 'wb') as f:
            pickle.dump(estado, f)

    @staticmethod
    def carregar_jogo(nome_arquivo='save01.sav'):
        try:
            with open(os.path.join(SaveSystem.SAVE_DIR, nome_arquivo), 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None
