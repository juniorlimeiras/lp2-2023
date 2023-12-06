from historico import Historico
class Conta:
    #Atributo de classe
    _total_contas = 0
    #Atributo __slots__
    __slots__ = ['numero', 'titular', '_saldo', '_limite', 'historico']
    #Método de inicialização da classe conta
    def __init__(self, n, cliente, s, l):
        self.numero = n         #Atributos de objeto
        self.titular = cliente
        self._saldo = s
        self._limite = l
        self.historico = Historico()
        Conta._total_contas += 1

    #@staticmethod #Métodos estáticos não podem ser reescritos na herança
    @classmethod
    def get_total_contas(cls):
        return cls._total_contas

    #Métodos de Acesso com anotações para o atributo _limite
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        self._limite = valor

    #Métodos para o atributo _saldo
    def sacar(self, valor):
        if valor > self._saldo:
            return False
        else:
            self._saldo -= valor
            self.historico.transacoes.append(f'Saque de {valor}')
            return True

    def depositar(self, valor):
        self._saldo += valor
        self.historico.transacoes.append(f'Depósito de {valor}')

    def ver_saldo(self):
        print(f'Número: {self.numero} Saldo:{self._saldo}')

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            self.historico.transacoes.append(f'Transferência da conta '
                                             f'{self.numero} de {valor} '
                                             f'para conta '
                                             f'{destino.numero}')
            return True
        else:
            return False
    #Método __str__ reescrito
    def __str__(self):
        return f'Número:{self.numero}, Titular:{self.titular}'