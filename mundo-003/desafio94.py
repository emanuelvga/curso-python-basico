# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = dict()
grupo = list()
contmulher = soma = idade = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True: 
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if pessoas['sexo'] == 'F':
            contmulher += 1
        if pessoas['sexo'] in 'MF':
            break
        print('Error digite um sexo valido M ou F')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    grupo.append(pessoas.copy())
    while True:
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()
        if continuar in 'SN':
            break
        print('Erro digite apenas S ou N')
    if continuar == 'N':
        break
print('-' * 40)
media = soma / len(grupo)
print(f'foram cadastradas {len(grupo)} pessoas. ')
print(f'A média de idade é {media}')
print(f'As mulheres cadastradas foram ', end=' ')
for p in grupo:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end=' ')
print()
print('As pessoas com a idade acima da media foram ', end=' ')
for p in grupo:
    if p['idade'] >= media:
        print('    ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('<<<ENCERRANDO>>>')


  
    