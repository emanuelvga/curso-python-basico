from ex115.biblioteca.interface1.linhaecabeçalho import*


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
            return False
    else:
        return True



def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve algum problema na criação do arquivo. ')
    else:
        print(f'Arquivo {nome} criado com sucesso. ')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo. ')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.readlines())

    



