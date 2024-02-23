class Estagiario():
    def __init__(self, nome, cpf, bolsa, senha):
        self._nome = nome
        self._cpf = cpf
        self._bolsa = bolsa
        self._senha = senha

    # def autenticar(self, senha):
    #     if senha == self._senha:
    #         return True
    #     else:
    #         return False

    def __str__(self):
        return f'{self._nome} {self._cpf}'