# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
turma = list()
while True:
    nome = (str(input('Nome do aluno: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    turma.append([nome, [nota1, nota2], media])
    resposta = str(input('Deseja continuar? [S/N]'))
    if resposta in 'Nn':
        break
print('-' * 40)
print('               Boletim               ')
print('-' * 40)
print(f'{"No":<4}{"Nome":<10}{"Media":>8}')
for i, c in enumerate(turma):
    print(f'{i:<4}{c[0]:<10}{c[2]:>8}')
while True:
    print('-' * 40)
    verificar = int(input('quer saber a nota de algum aluno? 999 para sair: '))
    if verificar == 999:
        print('Finalizando...')
        break
    if verificar <= len(turma) -1:
        print(f'notas de {turma[verificar][0]} são {turma[verificar][1]}')
print('volte sempre')
        
    

