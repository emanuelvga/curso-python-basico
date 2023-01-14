from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('os numeros sorteados foi:', end= ' ')
for numero in n:
    print(numero, end=' ')
print(f'\nO maior numero foi {max(n)}')
print(f'O menor valor foi {min(n)}')