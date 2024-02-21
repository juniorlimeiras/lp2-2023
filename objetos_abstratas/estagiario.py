class Estagiario():
    def __init__(self, nome, cpf, bolsa):
        self._nome = nome
        self._cpf = cpf
        self._bolsa = bolsa

    def __str__(self):
        return f'{self._nome} {self._cpf}'