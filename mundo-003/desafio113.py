def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERROR, por favor digite um número inteiro válido. \033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31Entrada de dados interrompida pelo usuário.\033[m ')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERROR, por favor digite um número real válido. \033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31Entrada de dados interrompida pelo usuário.\033[m ')
            return 0
        else:
            return n






n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'O número inteiro digitado foi {n1}')
print(f'O número real digitado foi {n2}')