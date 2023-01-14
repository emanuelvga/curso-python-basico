def aumentar(preço = 0, taxa = 0, formatado=False):
    res = preço + (preço * taxa / 100)
    return res if formatado is False else moeda(res)

def metade(preço = 0, formatado=False):
    res = preço / 2
    return res if formatado is False else moeda(res)

def dobro(preço = 0, formatado=False):
    res = preço * 2
    return res if formatado is False else moeda(res)

def diminuir(preço = 0, taxa = 0, formatado=False):
    res = preço - (preço * taxa / 100)
    return res if formatado is False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 40)
    print('RESUMO DO VALOR' . center(30))
    print('-' * 40)
    print(f'Preço Analizado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Aumento de {taxaa} %: \t{aumentar(preço, taxaa, True)}')
    print(f'Desconto de {taxaa} %: \t{diminuir(preço, taxar, True)}')
    print('-' * 40)
