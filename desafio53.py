#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
print("=" * 20)
print("IDENTIFICADOR DE PALINDROMO")
print("=" * 20)
frase = str(input("Digite uma frase: ")).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f"é uma palindromo pois {junto} lido inversamente é {inverso}")
else:
    print("não é um palindromo")
