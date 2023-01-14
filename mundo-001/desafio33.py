#faça um programa que leia 3 numeros e diga qual é o maior
print("QUAL É O MAIOR")
a = int(input("Digite o primeiro numero: "))
b = int(input("digite o segundo numero: "))
c = int(input("digite o terceiro numero: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f"o menor é {menor}")
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"o maior numero é {maior}")
