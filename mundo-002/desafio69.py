# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
sexo = continuar = ' '
contidade = homens = mulheres = 0
while True:
    idade = int(input('Qual sua idade? '))
    while sexo not in 'HM':
        sexo = str(input('Qual o seu sexo? [H/M] ')).strip().upper()[0]
    while continuar not in 'SN':
            continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    else:
        print('_' * 40)
    if sexo in 'H':
        homens += 1
    if sexo in 'M' and idade < 20:
        mulheres += 1
    if idade >= 18:
        contidade += 1
    sexo = ' '
    continuar = ' '
print(f'A quantidade de pessoas maior de 18 anos é {contidade}, foram {homens} homens cadastrados e {mulheres} mulheres com menos de 20 anos de idade.')
