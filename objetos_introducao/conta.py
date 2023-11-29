from objetos_introducao.historico import Historico
class Conta:
    def __init__(self, n, cliente, s, l):
        self.numero = n
        self.titular = cliente
        self.saldo = s
        self.limite = l
        self.historico = Historico()


    def sacar(self, valor):
        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f'Saque de {valor}')
            return True

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Depósito de {valor}')

    def ver_saldo(self):
        print(f'Número: {self.numero} Saldo:{self.saldo}')

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

    def __str__(self):
        return f'Número:{self.numero}, Titular:{self.titular}'