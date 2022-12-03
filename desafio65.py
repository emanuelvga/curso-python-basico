#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    num = int(input('digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar [s/n]')).upper().strip()[0]
media = soma / quant
print(f'foram digitados {quant} e sua media foi {media}')
print(f'maior valor foi {maior} e o menor valor foi {menor}')
    

