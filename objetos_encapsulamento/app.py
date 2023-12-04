from conta import Conta
from cliente import Cliente

cliente = Cliente('Manoel', 'Limeira', '11111111111')
c1 = Conta(1, cliente, 1000, 100)
c1.limite = 200
print(c1.limite)
#print(c1._Conta__saldo) #Mesmo com os __ (encapsulamento)
                        #conseguimos acessar o saldo
print(vars(c1))
s = c1._saldo   #Isso não deve ser digitado nunca
c1.ver_saldo()
# c2 = c1 #Passagem de referências
c2 = Conta(2, 'Limeira', 2000, 200)
#c3 = Conta(1, 'Manoel', 1000, 100)

c2.depositar(100)
c2.sacar(50)
c2.transferir(c1, 500)
c2.ver_saldo()
c1.ver_saldo()
c2.historico.imprimir_extrato()
print(c1.__str__())
print(c1)
#print(id(c1))
#print(id(c2))
#print(id(c3))
# c1.depositar(100)
# c1.sacar(300)
#print(c1.__dict__) #imprime um dicionário
#print(dir(c1)) # mostra todos os recursos
#print(vars(c1))
# print(c1.__str__())
# print(str(c1))
# print(c1)

#Total de contas
print(Conta.get_total_contas())