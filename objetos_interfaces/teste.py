from cliente import Cliente
from gerente import Gerente
from sistema import Sistema
from secretaria import SecretariaAdministrativa
from presidente import Presidente
from estagiario import Estagiario
from diretor import Diretor
from autenticavel import Autenticavel

c1 = Cliente('Fulano', '123')
g1 = Gerente('Gerente', '0000000', 9000, 'g@g.com', '1234', 10)
s1 = SecretariaAdministrativa('Secretaria', '1111111', 2000, '12345')

# print(c1.autenticar('123'))
# print(g1.autenticar('1234'))
# print(s1.autenticar('12345'))

p1 = Presidente('Getulio', '9999999', 39000)
e1 = Estagiario('Lascado', '0000000', 700, 'senha')
d1 = Diretor('Geirto', '111111', 6000, 'email@geirto', '123456', 1, 3)

Autenticavel.register(Estagiario)

sistema = Sistema()
lista = [c1, g1, s1, e1, d1, p1]
for i in lista:
    sistema.login(i)