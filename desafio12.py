# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
print("calculadora de 5% de desconto")
prod = float(input("Digite o valor do produto: "))
eco = prod * 5 / 100
des = prod - eco
print(f"o valor do produto com desconto foi de: {des:.2f}")
print(f"você obteve uma economia de {eco:.2f} reais")
