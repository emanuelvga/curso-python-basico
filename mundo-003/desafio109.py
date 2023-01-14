import utilidades.moeda as moeda


n = float(input('digite o preço: '))
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'Aumentando 10% é {moeda.aumentar(n, 10, True)}')
print(f'Diminuindo 13% é {moeda.diminuir(n, 13, True)}')