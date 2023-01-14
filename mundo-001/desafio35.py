# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b
print("FORMARA UM TRIANGULO?")
a = float(input("digite o primeiro comprimento de a: "))
b = float(input("digite o segundo comprimento de b: "))
c = float(input("digite o terceiro comprimento de c: "))
if a < b + c and b < a + c and c < a + b:
    print("Formara um triangulo")
else:
    print("Não formara um triangulo")
