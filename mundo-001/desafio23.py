#faça um programa que leia do 0 a 9999 e mostre na tela cada um dos digitos separados
#ex: digite um numero: 1234
#unidade 4, dezena 3, centena 2, milhar 1.
numero = int(input("digite um numero com 4 algarismos: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f"Milhar: {m}")
print(f"Centena: {c}")
print(f"Dezena: {d}")
print(f"Unidade: {u}")
