# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    tam = len(msg) + 4
    print(f'{"-" * tam}')
    print(f'  {msg}')
    print(f'{"-" * tam}')



escreva('jamaica')
escreva('Girocoptor')
escreva('Emannuel Pereira de Oliveira')
