#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porçao inteira.
#ex: digite um numero: 6.127
#O numero 6.127 tem a parte inteira 6.
from math import trunc
num = float(input("Digite um numero real: "))
inteiro = trunc(num)
print(f"o número {num} tem sua parte inteira {inteiro}")
