lista = [i if i%2==0 else i*i for i in range(11)]
lista2 = [i for i in range(11) if i%2==0 if i<7 if i>3]
frutas = ['    abacate', 'abacaxi   ','   banana']
lista3 = [len(f.strip()) for f in frutas]
print(lista)
print(lista2)
print(lista3)