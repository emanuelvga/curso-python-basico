#Crie um programa que leia dois valores e mostre um menu na tela.
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
print("CALCULADORA WHILE.")
primeirovalor = int(input("Digite um valor: "))
segundovalor = int(input("digite outro valor: "))
operacao = 0
while operacao != 5:
    print(" 1  somar")
    print(" 2  multiplicar")
    print(" 3  maior")
    print(" 4  novos números")
    print(" 5  sair do programa")
    operacao = int(input("Qual operação deseja fazer? "))
    soma = primeirovalor + segundovalor
    multiplicar = primeirovalor * segundovalor
    maior = primeirovalor
    if operacao == 1:
        primeirovalor + segundovalor
        print(f"a soma entre {primeirovalor} e {segundovalor} é {soma}")
    elif operacao == 2:
        primeirovalor * segundovalor
        print(f"a multiplicação entre {primeirovalor} e {segundovalor} é {multiplicar}.")
    elif operacao == 3:
        if maior > segundovalor:
            print(f"o maior valor é {maior}")
        elif maior < segundovalor:
            print(f"o maior valor é {segundovalor}")
        else:
            print("os valores sao iguais")
    elif operacao == 4:
        primeirovalor = int(input("Digite um valor: "))
        segundovalor = int(input("digite outro valor: "))
    elif operacao == 5:
        print("SAINDO...")
    elif operacao != range(1, 5):
        print("opçao invalida")
    print('='* 30)
