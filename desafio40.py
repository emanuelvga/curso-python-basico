#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
nota = float(input("Primeira nota: "))
nota1 = float(input("Segunda nota: "))
media = (nota + nota1) / 2
if media < 5:
    print(f"REPROVADO, pois sua media foi {media:.2f}")
elif media >= 5 and media <= 6.9:
    print(f"RECUPERAÇÃO, pois sua media foi {media:.2f}")
elif  media >= 7:
    print(f"APROVADO, a sua media foi {media:.2f}")
