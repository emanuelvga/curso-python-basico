#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
#a² = b² + c²
from math import hypot
catetooposto = float(input("Qual o valor do cateto oposto? "))
catetoadjacente = float(input("Qual o valor do cateto adjacente? "))
hipotenusa = hypot(catetooposto, catetoadjacente)
print(f"o resultado da hipotenusa é {hipotenusa:.2f} ")
