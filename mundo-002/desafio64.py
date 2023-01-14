n = 0
c = n
vezes = 0
n = int(input("digite qualquer valor.[999 para parar] "))
while n != 999:
    c += n
    vezes += 1
    n = int(input("digite qualquer valor.[999 para parar] "))
print(f"voce digitou {vezes} numeros e a soma entre eles foi {c}")
    



