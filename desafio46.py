# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
from datetime import date
for contador in range(10, -1, -1):
    print(contador)
    sleep(2)
print(f"feliz {date.today().year + 1}")
