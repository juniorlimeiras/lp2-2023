class Conta:
    def __init__(self, n, t, s, l):
        self.numero = n
        self.titular = t
        self.saldo = s
        self.limite = l

    def sacar(self, valor):
        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
            return True

    def depositar(self, valor):
        self.saldo += valor

    def ver_saldo(self):
        print(f'Número: {self.numero} Saldo:{self.saldo}')