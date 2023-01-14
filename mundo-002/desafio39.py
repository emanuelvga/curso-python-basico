# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anonasc = int(input("Digite seu ano de nascimento: "))
anoatual = date.today().year
idade = anoatual - anonasc
if anoatual - anonasc == 18:
    print(f"aliste-se, pois você tem a idade exata")
elif anoatual - anonasc < 18:
    print(f"ainda falta {18 - idade} ano(s) ")
elif anoatual - anonasc > 18:
    print(f"ja passou {idade - 18} anos do prazo ")
