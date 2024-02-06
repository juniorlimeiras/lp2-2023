from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    @abstractmethod
    def verifica_id(self, id):
        pass


class PessoaFisica(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
    # def verifica_id(self, id):
    #     #Vefiriacação do cpf
    #     print('Verificado')

#p1 = Pessoa('Limeira')
p2 = PessoaFisica('Limeira')
print(p2.get_nome())
p2.verifica_id('99999999999')