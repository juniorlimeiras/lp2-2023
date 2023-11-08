def imprime_linhas():
    print('Linha 1')
    yield 1
    print('Linha 2')
    yield 2
    print('Linha 3')
    yield 3
    #return 'Fim da Função Imprimir'

#i = imprime_linhas()
#print(i)

gerador = imprime_linhas()
print(next(gerador))
print(next(gerador))
print(next(gerador))