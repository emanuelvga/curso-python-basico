from gettext import find


tupla = ('palmeiras', 'internacional', 'flamengo', 'fluminense', 'corintians', 'atletico PR', 'atletico MG', 'america MG', 'fortaleza', 'botafogo', 'santos', 'sao paulo', 'bragantino', 'goiais', 'curitiba', 'ceara SC', 'cuiaba', 'atletico GO', 'avai', 'juventude')
print('=' * 100)
print(f'Os 5 primeiros colocados são {tupla[0:5]}')
print('=' * 100)
print(f'Os ultimos 4 colocados são {tupla[-4:]}')
print('=' * 100)
print(f'Os times em ordem alfabética fica: {sorted(tupla)}')
print('=' * 100)
print('o time da chapecoense nao se encontra na tupla')
print(f'o fortaleza esta na {tupla.index("fortaleza")+1} posiçao.')