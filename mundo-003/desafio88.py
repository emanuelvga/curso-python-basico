from random import randint
from time import sleep
print('-' * 40)
print('          MEGA SENA SORTEIO          ')
print('-' * 40)
lista = []
num = 0
n = int(input('Quantos sorteios quer fazer? '))
print(f'SORTEANDO {n} JOGOS')
for d in range(1, n + 1):
    for num in range(1, 7):
        if num not in lista:
            num = randint(0, 60)
            lista.append(num)
        sleep(0.2)
    lista.sort()
    print(f'Jogo numero {d} {lista}')
    lista.clear()