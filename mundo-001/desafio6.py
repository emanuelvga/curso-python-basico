#crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input("Digite um número: "))
dob = n1 * 2
tri = n1 * 3
sqrt = n1**(0.5)
print(
    f" o dobro é: {dob},\n o triplo é: {tri},\n e a raiz quadrada é: {sqrt:.2f} "
)
