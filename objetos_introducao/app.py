from teste.conta import Conta

c1 = Conta(1, 'Manoel', 1000, 100)
c1.ver_saldo()
c1.depositar(100)
c1.sacar(300)
print(c1.__dict__)
print(dir(c1))
print(vars(c1))
print(c1.__str__())
print(str(c1))
print(c1)