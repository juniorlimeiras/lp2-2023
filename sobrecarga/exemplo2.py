class Sobrecarga:
    def __init__(self, *args):
        self._tam = len(args)

    def __str__(self):
        if self._tam == 0:
            return 'Zero'
        elif self._tam == 1:
            return 'Um'
        elif self._tam == 2:
            return 'Dois'

s0 = Sobrecarga()
s1 = Sobrecarga(1)
s2 = Sobrecarga(1,2)
print(s0, s1, s2)