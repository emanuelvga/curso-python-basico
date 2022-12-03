# faça um programa que veja se o nosso ano atual é bisexto
from datetime import date
print("ANO ATUAL É BISEXTO?")
ano = int(input("Que ano quer analizar?, Para analizar o ano atual digite 0: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ANO DE {ano} É BISSEXTO")
else:
    print(f"O ANO DE {ano} NÃO É BISSEXTO")
