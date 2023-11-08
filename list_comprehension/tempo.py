import time

def gera(n):
    for i in range(n):
        yield (i*i)

def loop(n):
    lista = []
    for i in range(n):
        lista.append(i*i)
    return lista
def listc(n):
    return [i*i for i in range(n)]

inicio = time.time()
listc(10**7)
fim = time.time()
print(f'Tempo 1: {fim-inicio}')
inicio = time.time()
loop(10**7)
fim = time.time()
print(f'Tempo 2: {fim-inicio}')
inicio = time.time()
for n in gera(10**7):
    continue
fim = time.time()
print(f'Tempo 3: {fim-inicio}')

