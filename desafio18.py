#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno, e tangente desse angulo.
from math import sin, cos, tan, radians
angulo = float(input("Qual o valor do ângulo? "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f"O seno é {seno:.2f}\n O cosseno é {cosseno:.2f}\n O tangente é {tangente:.2f}")
