#Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando 50 cents por km para viagens de ate 200km de distacia e 45 para viagens mais longas.
print("CALCULANDO A PASSAGEM")
distancia = int(input("Digite a distancia de uma cidade a outra KM:"))
taxa = distancia * 0.50
taxa2 = distancia * 0.45
if distancia <= 200:
    print(f"sua taxa será de {taxa:.2f}$")
else:
    print(f"sua taxa foi de {taxa2:.2f}$")
