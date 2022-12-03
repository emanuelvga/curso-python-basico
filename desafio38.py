#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais
n = int(input("Digite um número: "))
n1 = int(input("Digite outro número: "))
if n > n1:
    print(f"o primeiro valor {n} é maior. ")
elif n < n1:
    print(f"o segundo valor {n1} é maior.")
else:
    print(f"os dois valores são iguais.")
    