from abc import ABC, abstractmethod


class Funcionario(ABC):
    # def __init__(self, nome, cpf, salario, email):
    #     self._nome = nome
    #     self._cpf = cpf
    #     self._salario = salario
    #     self._email = email

    @abstractmethod
    def get_bonifica(self):
        pass
