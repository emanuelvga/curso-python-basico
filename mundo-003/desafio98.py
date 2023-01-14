# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep
def contador(i, f ,p):
    print('-=' * 20)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    sleep(2)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            sleep(0.3)
            print(f'{cont}', end=' ')
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            sleep(0.3)
            print(f'{cont}', end=' ')
            cont -= p
        print('FIM')




contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('INICIO: '))
fim = int(input('FIM: '))
pas = int(input('PASSOS: '))
contador(ini, fim, pas)
