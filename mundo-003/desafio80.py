valor = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valor[len(valor) - 1]:    # or elif n > valor[-1]..... faz a mesma coisa que o codigo acima.
        valor.append(n)
        print('Item adicionado ao final da lista. ')
    else:
        pos = 0
        while pos < len(valor):
            if n <= valor[pos]:
                valor.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-' * 50)
print(f'Os valores digitados foram {valor}')
