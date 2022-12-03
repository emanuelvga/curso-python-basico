#crie um programa que leia uma frase e mostre: quantas vezes aparece a letra 'a', em que posiçao ela aparece a primeira vez, em que posiçao ela aparece pela ultima vez.
letra = str(input("Digite uma frase: ")).strip().lower()
print(f"A letra (a) aparece {letra.count('a')} vezes")
print(f"A primeira vez que aparece a letra (a) é no {letra.find('a') + 1}º caracter.")
print(f"A ultima vez que aparece a letra (a) é no {letra.rfind('a') + 1}º caracter.")
