#Crie um programa que leia o nome de uma pessoa e diga se contem SILVA no nome
nome = str(input("Digite seu nome completo: ")).strip().upper()
print(f"vejamos se tem Silva no seu nome: {'SILVA' in nome}")
