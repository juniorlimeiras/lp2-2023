class Historico:
    def __init__(self):
        self.transacoes = []

    def imprimir_extrato(self):
        for i in self.transacoes:
            print(i)