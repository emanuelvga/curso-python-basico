import utilidades.moeda as moeda


n = float(input('digite o preço: '))
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'Aumentando 10% é {moeda.moeda(moeda.aumentar(n,10))}')