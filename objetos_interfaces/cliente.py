from autenticavel import Autenticavel
class Cliente(Autenticavel):
    def __init__(self, nome, senha):
        self._nome = nome
        self._senha = senha

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    def autenticar(self, senha):
        if senha == self._senha:
            return True
        else:
            return False
