from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, email, senha, qtde):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._email = email
        self._senha = senha
        self._qtde_func = qtde

    def autentica(self, senha):
        if senha == self._senha:
            return True
        else:
            return False

    def get_bonifica(self):
        return self._salario * 1.3