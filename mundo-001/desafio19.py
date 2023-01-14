# Um professor quer sortear um dos seus 4 alunos para apagar o quadro, faça um programa que ajude ele, lendo o nome deles e ecrevendo o nome do escolhido.
from random import choice
aluno1 = input("primeiro aluno:")
aluno2 = input("segundo aluno:")
aluno3 = input("terceiro aluno:")
aluno4 = input("quarto aluno:")
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista)
print(f"o aluno sorteado foi {sorteio}")
