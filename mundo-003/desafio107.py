import utilidades.moeda as moeda


n = float(input('digite o preço: '))
print(f'O dobro de ${n} é ${moeda.dobro(n)}')
print(f'A metade de ${n} é ${moeda.metade(n)}')
print(f'Aumentando 10% é ${moeda.aumentar(n,10)}')