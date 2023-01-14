# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint
print('vamos jogar par ou impar? ')
cont = comp = 0
while True:
    comp = randint(1,10)
    n = int(input('escolha um valor: '))
    soma = n + comp
    pori = ' '
    while pori not in 'PI':
        pori = str(input('[P/I]')).upper().strip()[0]
    print(f'você jogou {n} e o computador jogou {comp} o resultado foi {soma}')
    if soma % 2 == 0 and pori in 'Pp':
        print('Deu par voce venceu')
        cont += 1
        print('-' * 30)
    elif soma % 2 != 0 and pori in 'Ii':
        print('Deu impar voce venceu')
        cont += 1
        print('-' * 30)
    elif soma % 2 == 0 and pori in 'Ii':
        print('voce perdeu, pois deu Par')
        print('-' * 30)
        break
    elif soma % 2 != 0 and pori in 'Pp':
        print('voce perdeu, pois deu impar')
        print('-' * 30)
        break
print(f'voce ganhou {cont} seguidas')
