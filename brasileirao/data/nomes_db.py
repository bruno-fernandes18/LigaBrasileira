class NomesDB:
    NOMES_MASCULINOS = ['Joao', 'Pedro', 'Lucas']
    NOMES_FEMININOS = ['Maria', 'Ana', 'Juliana']
    SOBRENOMES = ['Silva', 'Souza', 'Oliveira']

    @staticmethod
    def gerar_nome(genero='M'):
        import random
        if genero == 'F':
            nome = random.choice(NomesDB.NOMES_FEMININOS)
        else:
            nome = random.choice(NomesDB.NOMES_MASCULINOS)
        sobrenome = random.choice(NomesDB.SOBRENOMES)
        return f"{nome} {sobrenome}"
