#Escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80km, mostra uma mensagem dizendo que ele foi multado, a multa vai custa7$ por km ultrapassado.
print("RADAR DE 80KM/H")
km = int(input("Quantos km/h? "))
multa = (km - 80) * 7
if km > 80:
    print(f"voce foi multado em {multa}$, pois excedeu a velocidade maxima permitida ")
else:
    print("faça uma boa viagem")
