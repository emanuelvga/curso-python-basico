 #A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
anodenasc = int(input("Digite o ano de nascimento do atleta: "))
idade =  date.today().year - anodenasc
categoria = idade
if categoria <= 9:
    print(f"{categoria} anos categoria MIRIM")
elif categoria > 9 and categoria <= 14:
    print(f"{categoria} anos categoria INFANTIL")
elif categoria > 14 and categoria <= 19:
    print (f"{categoria} anos categoria JUNIOR")
elif categoria > 19 and categoria <= 25:
    print(f"{categoria} anos  categiria SENIOR")
else:
    print(f"{categoria} anos categoria MASTER")
