#  Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
continuar = ' '
total = maisdemil = cont = barato = 0
menor = ''
while True:
    produto = str(input('Qual o nome do produto? '))
    valor = float(input('Quanto custa? '))
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    print('_' * 40)
    total += valor
    if valor > 1000:
        maisdemil += 1
    cont += 1
    if cont == 1 or valor < barato:
        barato = valor
        menor = produto
    if continuar == 'N':
        break
    continuar = ' '   
print(f'O total gasto na compra foi {total:.2f}')
print(f'foram {maisdemil} produtos acima de 1000$$')
print(f'O nome do produto mais barato é {menor} , e custou {barato:.2f}')
