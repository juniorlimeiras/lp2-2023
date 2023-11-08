def geradora():
    for i in range(10**8):
        yield i

g = geradora()
#for i in g:
#    print(i)
#g = geradora()
lista = list(g)