class CidadesDB:
    CIDADE_ESTADOS = {
        'Rio de Janeiro': 'RJ',
        'Sao Paulo': 'SP',
    }

    @staticmethod
    def obter_estado(cidade: str):
        return CidadesDB.CIDADE_ESTADOS.get(cidade, 'BR')
