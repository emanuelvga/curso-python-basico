lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    resp = str(input('Deseja continuar?[S/N] '))
    if resp in 'Nn':
        break
print(f'foram digitados {len(lista)} numeros que sao: {lista}')
print(f'os pares são {listapar}')
print(f'os impares são {listaimpar}')
    

    
