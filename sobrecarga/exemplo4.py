class Tempo:
    def __init__(self, h=0, m=0, s=0):
        self._h = h
        self._m = m
        self._s = s
    def __str__(self):
        return f'{self._h:02}:{self._m:02d}:{self._s:02.0f}'
t1 = Tempo(0o2,0o3,50)# 0o2 é uma representação octal
print(t1)