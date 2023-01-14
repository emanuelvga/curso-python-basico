# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
funcionario = dict()
funcionario['nome'] = str(input('Nome: '))
funcionario['nascimento'] = int(input('Ano de nascimento: '))
funcionario['idade'] = datetime.now().year - funcionario['nascimento']
funcionario['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if funcionario['ctps'] != 0:
    funcionario['contratação'] = int(input('Ano de contratação: '))
    funcionario['salario'] = float(input('Salário: '))
    funcionario['aposentadoria'] = funcionario['idade'] + ((funcionario['contratação'] + 35) - datetime.now().year)
print('-' * 40)
for k, v in funcionario.items():
    print(f'O {k} tem valor {v}')
    