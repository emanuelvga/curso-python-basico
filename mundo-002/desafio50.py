#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
for contador in range(1, 7):
    numero = int(input("Digite valores: "))
    if numero % 2 == 0:
        soma += numero
print(f"a soma dos numeros pares foram = {soma}")
