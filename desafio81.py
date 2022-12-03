lista = []
continuar = ' '
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
    continuar = ' '
lista.sort(reverse = True)
print(f'Foram digitados {len(lista)} numeros')
print(f'A lista ordenada de forma decrescente {lista}')
if 5 in lista:
    print(f'O numero 5 esta na lista. ')
else:
    print(f'O 5 nao esta na lista. ')