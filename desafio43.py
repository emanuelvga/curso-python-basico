#  Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# # - Acima de 40: Obesidade Mórbida
peso = float(input("Qual o seu peso? "))
altura = float(input("qual a sua altura? "))
imc = (peso / altura**2)
print(f"{imc:.2f} de IMC")
if imc < 18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc <= 24.99:
    print("seu peso é normal")
elif imc >= 25 and imc <= 29.99:
    print("sobrepeso")
elif imc >= 30 and imc <= 40:
    print("obeso")
else:
    print("obesidade morbida")
