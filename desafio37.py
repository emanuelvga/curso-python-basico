# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input("Digite um número: "))
print(f"digite (1) para converter {n} para binario ")
print(f"digite (2) para converter {n} para octal ")
print(f"digite (3) para converter {n} hexadecimal ")
escolheu = int(input("Qual conversão deseja fazer? "))
if escolheu == 1:
    print(f"A conversão para binario de {n} é {bin(n)[2:]}")
elif escolheu == 2:
    print(f"A conversão de {n} para octal é {oct(n)[2:]}")
elif escolheu == 3:
    print(f"A conversao de {n} para hexadecimal é {hex(n)[2:]}")
else:
    print("opçao invalida")
    