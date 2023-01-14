from ex115.biblioteca.interface1.linhaecabeçalho import*
from ex115.biblioteca.arquivo.listadenomes import*
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:     
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair'])
    if resposta == 1:
        # Opçao de  listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        print('opção - 2')
    elif resposta == 3:
        print('Saindo do Sistema ... até logo')
        break
    else:
        print('\033[31mERRO digite uma opção válida.\033[m ')
    sleep(2.0)

