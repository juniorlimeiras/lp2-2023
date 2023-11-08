def soma(*args):
    r = 0
    print(type(args))
    for i in args:
        r += i
    return r

print(soma(1,2,3,4,5,6))
#args precisa de uma tupla para funcionar.
#print(soma(tuple([i for i in range(10)])))
