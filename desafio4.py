# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas informaçoes possiveis sobre ele.
algo = input("digite qualquer coisa  no teclado: ")
print(f"o timpo primitivo é {type(algo)}")
print(f"é numérico? {algo.isnumeric()}")
print(f"é alfabético? {algo.isalpha()}")
print(f"é alfanumérico? {algo.isalnum()}")
print(f"é MAIÚSCULO? {algo.isupper()}")
print(f"é minusculo? {algo.islower()}")
print(f"é printavel? {algo.isprintable()}")
print(f"tem somente espaço? {algo.isspace()}")
print(f"esta capitalizada? {algo.istitle()}")
