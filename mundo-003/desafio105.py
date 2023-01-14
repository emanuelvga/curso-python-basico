# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

def notas(*n, sit=False):
    """
    > Função para analise de notas
    :param: n: Uma ou varias notas dos alunos
    :param: sit: Observa a media das notas e verifica se é boa, ruim ou razoavel.
    :param: return: Retorna um dicionario obtendo informações das notas.
    
    """
    r = dict()
    r ['total'] = len(n)
    r ['maior'] = max(n)
    r ['menor'] = min(n)
    r ['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'boa'
        elif r ['media'] >= 5:
            r['situação'] = 'rasoavel'
        else:
            r['situação'] = 'ruim'

    return r




resp = notas(6.5, 3.2, 4.0, 8.5, sit=True)
print(resp)
