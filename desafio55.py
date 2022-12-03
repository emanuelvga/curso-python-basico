#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input(f"{pessoas}° pessoa, Digite seu peso: "))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"o maior peso foi {maior}kg, e o menor foi de {menor}kg")



