#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
contador = 0
contador2 = 0
for pess in range(1, 8):
    anodenasc = int(input(f"Em que ano a {pess}c: "))
    idade = atual - anodenasc
    if idade >= 18:
        contador += 1
    else:
        contador2 += 1
print(f"obtiveram maior idade {contador} pessoas, e ainda sao menores {contador2} pessoas")
