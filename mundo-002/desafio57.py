#Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores M ou F. caso esteja errado, peça a digitaçao novamente ate ter um valor correto.
sexo = input("Digite seu sexo: [M/F] ").strip().upper()[0]
while sexo not in 'MF':
    sexo = input("opção invalida, por favor digite seu sexo: ").strip().upper()
print(f"sexo {sexo} registrado com sucesso.")
        
