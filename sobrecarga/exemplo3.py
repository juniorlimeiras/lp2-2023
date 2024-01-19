from functools import reduce
class Calculadora:
    def soma(self, *args):
        if type(args[0]) == str:
            total = ''
        else:
            total = 0
        for i in args:
            total += i
        return total

class Calculadora2:
    def soma(self, *args):
        return reduce(lambda a, b:a+b, args)

s1 = Calculadora()
print(s1.soma(2, 2, 2))
print(s1.soma(3.5, 4.5, 5.4, 3.4))
print(s1.soma('Py', 'thon ', 'é ', 'foda!'))
s2 = Calculadora2()
print(s2.soma(2, 2, 2))
print(s2.soma(3.5, 4.5, 5.4, 3.4))
print(s2.soma('Py', 'thon ', 'é ', 'muito foda!'))
