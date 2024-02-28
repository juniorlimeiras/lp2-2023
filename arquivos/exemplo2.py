arquivo = open('teste.txt', 'r')
linha = arquivo.readline()
# linha2 = arquivo.readline()
# print(linha1, end='')
# print(linha2, end='')
while linha != '':
    print(f'=>{linha}', end='')
    linha = arquivo.readline()
arquivo.close()
arquivo = open('teste.txt')
for i in arquivo:
    print(f'Outra forma de percorrer =>{i}',end='')
arquivo.close()