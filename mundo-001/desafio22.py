#crie um programa que leia o nome completo de uma pessoa:
#1 - o nome com todas as letras maiusculas.
#2 - o nome com toddas letras minusculas.
#3 - quantas letras ao todo, sem considerar espaços.
#4 - quantas letras tem o primeiro nome
nome = str(input("Digite seu nome completo: ")).strip()
primeironome = (nome.split()[0])
print(
    f"seu nome em maiusculo: {nome.upper()} \nSeu nome em minusculo: {nome.lower()} \nA contagem é: {len(nome) - nome.count(' ')}\nA contagem do primeiro nome é:{len(primeironome)}"
)
