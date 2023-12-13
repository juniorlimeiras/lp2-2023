from funcionario import Funcionario
from gerente import Gerente
from diretor import Diretor
f1 = Funcionario('Fulano', '99999999999', 10000, 'gmail')
print(f'{f1._nome} {f1.get_bonifica()}') #Não façam isso em casa
g1 = Gerente('Ciclano', '11111111111', 20000, 'uol', '123', 5)
print(f'{g1._nome} {g1.get_bonifica()}')
d1 = Diretor('Beltrano', '00000000000', 30000, 'pop', '1234', 6, 9)
print(f'{d1._nome} {d1.get_bonifica()}')
