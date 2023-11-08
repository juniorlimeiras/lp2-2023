iterador = iter('ABC')
print(iterador)
print(type(iterador))
for i in iterador:
    print(i)
#print(next(iterador))

lista = [1,2,3,4,5]
lista_i = iter(lista)
print(next(lista_i))

alunos = ['Maria', 'Julia', 'Mayara']
alunos_i = enumerate(alunos)
d = dict(alunos_i)
print(alunos_i)
#print(next(alunos_i)) #gera uma exceção StopIteration
print(d)
alunos_i = enumerate(alunos)
print(next(alunos_i))
for i,j in enumerate(alunos):
    print(f'Indice:{i}, Valor:{j}')

for i in reversed(alunos):
    print(f'Valor:{i}')

numeros = [10, 20, 30]
quadrados = (i**2 for i in numeros) #Função geradora
print(numeros[1])
print(next(quadrados))
print(next(quadrados))
print(next(quadrados))
#print(next(quadrados)) # Exceção, ou seja, percorreu até último elemento
quadrados = (i**2 for i in numeros) #Gerando um novo iterador
z = zip(numeros, quadrados)
print(type(z))
for i in z:
    print(i)