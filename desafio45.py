# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
print("-=" * 20)
print("JOKENPÔ")
print("-=" * 20)
print("opçoes")
print("1 - pedra ")
print("2 - papel ")
print("3 - tesoura ")
jogador = int(input("o que escolhera? "))
computador = randint(1, 3)
print(f"{jogador} vs {computador}")
if jogador == 1 and computador == 3:
    print("VOCE GANHOU POIS PEDRA AMASSA TESOURA ")
elif jogador == 1 and computador == 2:
    print("VOCÊ PERDEU POIS PAPEL EMBRULHA PEDRA ")
elif jogador == 1 and computador == 1:
    print("EMPATE PEDRA X PEDRA ")
elif jogador == 2 and computador == 2:
    print("EMPATE PAPEL X PAPEL ")
elif jogador == 2 and computador == 1:
    print("VOCE GANHOU POIS PAPEL EMBRULHA PEDRA ")
elif jogador == 2 and computador == 3:
    print("VOCÊ PERDEU POS TESOURA CORTA PAPEL ")
elif jogador == 3 and computador == 3:
    print("EMPATE TESOURA X TESOURA ")
elif jogador == 3 and computador == 1:
    print("VOCÊ PERDEU POIS PEDRA AMASSA TESOURA ")
elif jogador == 3 and computador == 2:
    print("VOCE GANHOU POIS TESOURA CORTA PAPEL ")
    