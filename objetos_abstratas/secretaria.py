from objetos_abstratas.funcionario import Funcionario
from abc import ABC


class Secretaria(Funcionario, ABC):
    pass

class SecretariaExecutiva(Secretaria):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonifica(self):
        return self._salario * 1.1 + 100

class SecretariaAdministrativa(Secretaria):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonifica(self):
        return self._salario + 100
