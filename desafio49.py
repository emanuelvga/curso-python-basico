# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input("Escolha um numero para saber a tabuada correspondente: "))
for tabuada in range(1, 11):
    print(f"{numero} x {tabuada} = {numero * tabuada}")
