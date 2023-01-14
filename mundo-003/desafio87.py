matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = maior = scol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um numero [{linha}, {coluna}]: '))
print('-' * 40)
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
        
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'a soma dos numeros pares foi {spar}')
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'a soma da coluna 3 é {scol}')
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior numero na linha 2 é {maior}')
