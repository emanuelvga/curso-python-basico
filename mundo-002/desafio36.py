#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print("Emprestimo bancario")
valordacasa = float(input("Qual o valor da casa? "))
salario = float(input("Qual valor do seu salario? "))
anos = int(input("Em quantos anos vai pagar? "))
meses = anos * 12
prestaçãomensal = valordacasa / meses
salarioparaprestaçao = (30 * salario / 100)
if prestaçãomensal > salarioparaprestaçao:
    print(f"SEU EMPRESTIMO NAO FOI APROVADO, POIS {prestaçãomensal:.2f}$ EXCEDEU 30% DO SEU SALARIO QUE É DE {salarioparaprestaçao:.2f}$")
else:
    print (F"PARABÉNS, SEU EMPRESTIMO FOI APROVADO POIS A PRESTAÇAO DE {prestaçãomensal:.2f}$ NÃO EXCEDEU 30% DO SEU SALARIO QUE É DE {salarioparaprestaçao:.2f}$")
