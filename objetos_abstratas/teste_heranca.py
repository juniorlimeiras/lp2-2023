from funcionario import Funcionario
from gerente import Gerente
from diretor import Diretor
from controleDeBonificacao import ControleDeBonificacao
from estagiario import Estagiario
from secretaria import SecretariaExecutiva, SecretariaAdministrativa
from presidente import Presidente
# f1 = Funcionario('Fulano', '99999999999', 10000, 'gmail')
# print(f'{f1._nome} {f1.get_bonifica()}') #Não façam isso em casa
g1 = Gerente('Ciclano', '11111111111', 2000, 'uol', '123', 5)
print(f'{g1._nome} {g1.get_bonifica()}')
d1 = Diretor('Beltrano', '00000000000', 2000, 'pop', '1234', 6, 9)
print(f'{d1._nome} {d1.get_bonifica()}')
se = SecretariaExecutiva('Maria', '000000000', 2000)
sa = SecretariaAdministrativa('Zefa', '000000000', 2000)
p = Presidente('L', '999999999', 10000)

controle = ControleDeBonificacao()
# controle.registra(f1)
lista = [g1, d1, se, sa, p]
for f in lista:
    controle.registra(f)
e1 = Estagiario('Estagiario Novo', '1223456778', 700)
controle.registra(e1)

print(ControleDeBonificacao.total())