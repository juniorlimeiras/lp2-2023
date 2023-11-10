from functools import reduce
Fatura = [('Net', 199.9),('Ifood', 999.87),('Gasolina', 678.0),('Formigão', 400)]
#Net - R$ 199.9
x, y = 10, 20
saida = [f'{i} - R$ {j}' for i,j in Fatura]
print(*saida, sep='\n')
print('Com laço')
#Um em cada linha
for s in saida:
    print(s)
#Solução com reduce
#print('#Solução com reduce')
print(reduce(lambda x,y : f'{x}{y[0]} - R${y[1]}\n', Fatura, '#Solução com reduce\n'))

#Ordenar
Fatura.sort(key = lambda x : x[1]) #sort altera a lista e retorna None
print(Fatura)

#Filtrar os gastos > 500
iterador_filter = filter(lambda x : x[1]>500, Fatura)
print(next(iterador_filter))
print(next(iterador_filter))
#print(next(iterador_filter)) #StopIteration
list_filter = list(filter(lambda x : x[1]>500, Fatura))
print(list_filter)
#Total da Fatura
total = reduce(lambda x,y : x + y[1], Fatura, 0)
print(total)
