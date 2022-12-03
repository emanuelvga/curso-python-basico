# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num=1, show=False):
    """
    > Calcular fatorial de um Número:
    :param n: O numero a ser calculado.
    :param show: (opcional), mostrar ou não a conta.
    :return: retorna o valor do fatorial de um numero n.
    
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

    
    

n = int(input('Digite um numero: '))
print(fatorial(n))
help(fatorial)