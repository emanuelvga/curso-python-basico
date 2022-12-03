#  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
valor = int(input("Digite o valor do produto "))
print("Qual opçao deseja? ")
print("1 - dinheiro a vista = 10 por cento de desconto")
print("2 - cartao a vista = 5 por cento de desconto")
print("3 - cartao parcelado em 2x = preço normal")
print("4 - cartao parcelado em 3x ou mais = 20 por cento de juros")
escolha = int(input("escolha uma das opçoes abaixo para compra do produto: "))
if escolha == 4 :
    escolha2 = int(input("Em quantas vezes? "))
din = valor - (valor * 0.1)
cartao = valor - (valor * 0.05)
cartao2x = valor
cartao3x = valor + (valor * 0.2)
if escolha == 1:
    print(f"o valor do produto com desconto de 10% será {din}")
elif escolha == 2:
    print(f"o valor do produto com desconto de 5% será {cartao}")
elif escolha == 3:
    print(f"o valor do produto parcelado em 2x sairá por 2 parcelas de {cartao2x / 2}$")
elif escolha == 4:
    print(f"o valor do produto parcelado em {escolha2}x sairá por {escolha2} parcelas de {(valor + valor * 0.2) / escolha2}$")

