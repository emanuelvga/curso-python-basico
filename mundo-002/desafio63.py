#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181...
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
print("=" * 30)
print("sequencia de fibo: ")
print("=" * 30)
n = int(input("Quantos termos quer ver? "))
termo1 = 0
termo2 = 1
print(f"{termo1} > {termo2}", end=' ')
cont = 3
while cont <= n:
    termo3 = termo1 + termo2
    print(f"> {termo3}", end=' ')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print("FINAL")



