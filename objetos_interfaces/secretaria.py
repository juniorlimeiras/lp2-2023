from funcionario import Funcionario
from abc import ABC
from autenticavel import Autenticavel


class Secretaria(Funcionario, Autenticavel):
    def autenticar(self, senha):
        if senha == self._senha:
            return True
        else:
            return False

class SecretariaExecutiva(Secretaria):
    def __init__(self, nome, cpf, salario, senha):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._senha = senha

    def get_bonifica(self):
        return self._salario * 1.1 + 100


class SecretariaAdministrativa(Secretaria):
    def __init__(self, nome, cpf, salario, senha):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._senha = senha

    def get_bonifica(self):
        return self._salario + 100
