# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print("AUMENTO DE SALARIO LVL 2")
salario = float(input("Digite seu salario: "))
aumento = (10 * salario / 100)
aumento2 = (15 * salario / 100)
if salario > 1250:
    print(f"Seu aumento foi de {aumento}")
else:
    salario <= 1250
    print(f"seu aumento foi de {aumento2}")
