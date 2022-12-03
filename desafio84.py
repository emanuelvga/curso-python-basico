from email.errors import InvalidMultipartContentTransferEncodingDefect


nomepeso = []
info = []
maior = menor = 0
while True:
    nomepeso.append(str(input('nome: ')))
    nomepeso.append(float(input('peso: ')))
    if len(info) == 0:
        maior = menor = nomepeso[1]
    else:
        if nomepeso[1] > maior:
            maior = nomepeso[1]
        if nomepeso[1] < menor:
            menor = nomepeso[1]
    info.append(nomepeso[:])
    nomepeso.clear()
    resp = str(input('continuar? [S/N]: '))
    print('-' * 50)
    if resp in 'Nn':
        break

    
print(f'Foram cadastradas {len(info)} pessoas')
print(f'O maior peso foi de {maior}kg, peso de', end=' ')
for p in info:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}kg, peso de', end=' ')
for p in info:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')


