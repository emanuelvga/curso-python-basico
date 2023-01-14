# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print("=" * 20)
print("10 TERMOS DE UMA PA")
print("=" * 20)
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razao da PA: "))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f"{termo} >", end=' ')
        termo += razao
        contador += 1
    print("Pausa")
    mais = int(input("quantos termos quer mostrar a mais? "))
print(f"foram usados {total} termos. ")
print("Fim")




