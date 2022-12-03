# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
maior = 0
somaidade = 0
mediaidade = 0
homemmaisvelho = 0
nomedohomem = ''
total20mulher = 0
for pessoas in range(1, 5):
    print(f"-----------{pessoas}°PESSOA -----------")
    nome = str(input("Digite seu nome:")).strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo: sendo h para homem e m para mulher ")).strip()
    somaidade += idade
    if pessoas == 1 and sexo in'Hh':
        homemmaisvelho = idade
        nomedohomem = nome
    if sexo in 'Hh' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomedohomem = nome
    if sexo in 'Mm' and idade < 20:
        total20mulher += 1

mediaidade = somaidade / 4
print(f"A media idade do grupo é {mediaidade}")
print(f"O homem mais velho tem {homemmaisvelho} anos e seu nome é {nomedohomem}")
print(f"Ao todo sao {total20mulher} mulher(s) menores que 20 anos")
   