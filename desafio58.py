#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print("ola sou seu computador, pensei em um numero de 0 a 10, tente adivinhar:")
computador = randint(0, 10)
tentativa = 0
aux = True
while aux:
    palpite = int(input("qual o seu palpite? "))
    tentativa += 1
    if palpite < computador:
        print("é mais")
    elif palpite > computador:
        print("é menos")
    if palpite == computador:
        print("winner")
        print(f"foram {tentativa} tentativas")
        aux = False