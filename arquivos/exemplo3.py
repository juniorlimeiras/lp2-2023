import random

with open('pares.txt', 'a') as pares:
    with open('impares.txt', 'a') as impares:
        for i in range(10):
            x = random.randint(1, 1000)
            if x % 2 == 0:
                pares.write(f'{x}\n')
            else:
                impares.write(f'{x}\n')
