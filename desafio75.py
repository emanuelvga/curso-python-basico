n1 = (int(input('digite um numero: '))),(int(input('digite um numero: '))),(int(input('digite um numero: '))),(int(input('digite um numero: ')))
print(f'voce digitou os valores: {n1}')
print(f'o valor nove apareceu {n1.count(9)} vezes')
if 3 in n1:
    print(f'o primeiro valor tres apareceu na posiçao {n1.index(3) + 1}')
else:
    print('nao tem o numero 3 na tupla')
print(f'os valores pares são:',end=' ')
for n in n1:
    if n % 2 == 0:
        print(n, end=' ')
