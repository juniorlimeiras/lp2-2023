#Como utlizar map para entrada de dados
#entrada = list(map(int, input().split()))

#Função anônima para somar elementos de duas listas
l1 = [1,2,3,4]
l2 = [5,6,7,8]
soma = list(map(lambda x,y:x+y, l1,l2))
print(type(soma))
#print(next(soma)) #só podemos usar next com iteradores
for s in soma:
    print(s)
#print(next(soma))
maior_que_10 = list(filter(lambda x: x>=10, soma))
print(maior_que_10)

produtos = [('ovos',10,4), ('pães',5,3),('tomate',6,2),('cenoura',4,1)]
produtos.sort(key=lambda x: x[2])
print(produtos)