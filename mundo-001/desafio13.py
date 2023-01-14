#faça um algoritmo que leia o salario de um funcionario e mostre o seu novo salario com 15% de aumento.
sal = float(input("seu antigo salario: "))
aum = sal * 15 / 100
nsal = sal + aum
print(f"seu novo salario aumentando em 15% é de: {nsal:.2f} reais ")
print(f"você obteve um aumento de {aum:.2f} reais ")
