# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
# jogadores = dict()
# jogo = list()
# print('Valores sorteados: ')
# for r in range(1, 5):
#     jogadores['resultados'] = randint(0, 6)
#     sleep(0.7)
#     print(f'O {r}o jogador pontuou {jogadores["resultados"]}')
#     jogo.append(jogadores['resultados'])
# for k in jogo:
#     print(f'{k}')
# print('-' * 40)
# print('RANK DOS JOGADORES')

jogo = {'jogador1': randint(0, 6),
        'jogador2': randint(0, 6),
        'jogador3': randint(0, 6),
        'jogador4': randint(0, 6)}
rank = list()
print('Valores Sorteados: ')
for k, v in jogo.items():
    sleep(1)
    print(f'{k} tirou {v} no dado')
print('-' * 40)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Rank dos jogadores')
print('-' * 40)
for i, v in enumerate(rank):
    print(f'{i + 1}o lugar: {v[0]} com {v[1]}.')

