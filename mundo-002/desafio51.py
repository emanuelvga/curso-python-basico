#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
print("=" * 20)
print("10 TERMOS DE UMA PA")
print("=" * 20)
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razao da PA: "))
decimo = primeiro + (11 - 1) * razao
for PA in range(primeiro, decimo , razao):
    print(PA, end=" → ")
print("acabou")
