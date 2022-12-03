#escreva um programa que faça o computador pensar em um numero interio de 0 a 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador. o programa devea escrever na tela se o usuario venceu ou perdeu.
print("JOGO DA ADIVINHAÇÃO")
from random import randint
from time import sleep
computador = randint(0, 5)
print("-" * 20)
print("VOU PENSAR EM UM NUMERO DE 0 A 5, TENTE ADIVINHAR")
print("-" * 20)
jogador = int(input("Em que número pensei?? "))
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print(f"Você ganhou, pois eu pensei justamente no número {computador}, parabéns!!!")
else:
    print(f"você perdeu, pois eu pensei no número {computador}, e não no número {jogador} tente novamente!!!")
