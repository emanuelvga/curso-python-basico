numeros = []
continuar = ' '
while True:
    n = int(input('digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado com sucesso!')
    else:
        print('Numeros repitidos, Não vou adicionar. ')
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]')).upper().strip()
    if continuar == 'N':
        break
    continuar = ' '
numeros.sort()
print(f'voce digitou os valores {numeros}')

        
    