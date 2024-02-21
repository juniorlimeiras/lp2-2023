from objetos_abstratas.funcionario import Funcionario


class Presidente(Funcionario):
    def get_bonifica(self):
        return self._salario * 1.5 + 1000

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

