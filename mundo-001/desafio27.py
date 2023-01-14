nome = str(input("Digite seu nome completo: ")).strip().title().split()
print(f"Analizando seu nome percebi que o primeiro é {nome[0]}")
print(f"E o seu ultimo nome é {nome[len(nome) - 1]}")
