class Cliente:
    def __init__(self, n, s, cpf):
        self.nome = n
        self.sobrenome = s
        self.cpf = cpf

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'