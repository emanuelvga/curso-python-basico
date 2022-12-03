# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def área(a, b):
    area = a * b 
    print(f'A área do terreno de {a} m x {b} m é {area}m²')
def lin():
    print('-' * 35)

print('Controle de Terrenos')
lin()
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
área(a, b)

