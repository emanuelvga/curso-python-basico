#  Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
vogais = 'A','E','I','O','U'
tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO',)
for palavras in tupla:
    print(f'\nNa palavra {palavras} temos', end=' ')
    for letras in palavras:
        if letras.upper() in 'AEIOU':
            print(letras, end=' ')

    
