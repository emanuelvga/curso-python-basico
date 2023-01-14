#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input("Digite um numero: "))
total = 0
for contador in range(1, numero + 1,):
    if numero % contador == 0:
        print('\033[33m', end=" ")
        total += 1
    else:
        print('\033[31m', end=" ")
    print(contador, end=" ")
print(f"\n\033[mO numero {numero} foi divisivel por {total} números")
if total == 2:
    print(f"por isso ele é primo")
else:
    print(f"por isso ele não é primo")
