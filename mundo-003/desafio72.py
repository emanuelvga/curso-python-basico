tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')
n = -1
while n not in range(0, 21):
        n = int(input('Digite um numero de 0 a 20: '))
        if n > 20:
            print('Numero invalido tente novamente.')
        elif n < 0:
            print('Numero invalido tente novamente.')
print(f'você digitou o número {tupla[n]}')
        
