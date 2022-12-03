#Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome 'santo'
cidade = str(input("Digite a cidade onde nasceu: ")).strip()
print(cidade.capitalize()[:5] == "Santo")
