# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(* num):
    cont = maior = 0
    print('-' * 45)
    print('Analizando valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} numeros')
    print(f'O maior valor informado foi {maior}')



#Programa Principal
maior(2, 5, 9, 3, 4 ,8 ,7)
maior(1, 2)
maior(3, 5, 6, 9, 10)
maior(5)
maior()