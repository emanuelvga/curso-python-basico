print("=" * 20)
print("10 TERMOS DE UMA PA")
print("=" * 20)
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razao da PA: "))
termo = primeiro
contador = 1
while contador <= 10:
    print(f"{termo} >", end=' ')
    termo += razao
    contador += 1


