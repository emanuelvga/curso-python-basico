# 2: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# # - ESCALENO: todos os lados diferentes
print("FORMARA UM TRIANGULO?")
a = float(input("digite o primeiro comprimento de a: "))
b = float(input("digite o segundo comprimento de b: "))
c = float(input("digite o terceiro comprimento de c: "))
if a < b + c and b < a + c and c < a + b:
    print("Formara um triangulo")
    if  a == b == c:
        print("EQUILATERO")
    elif a == b != c or a != b == c or a != c == b or a == c != b:
        print("ISÓCELES")
    elif a != b != c != a:
        print("ESCALENO")
else:
    print("Não formara um triangulo")
