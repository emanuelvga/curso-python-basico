#o mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos.faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada
from random import shuffle
aluno1 = input("primeiro aluno: ")
aluno2 = input("segundo aluno: ")
aluno3 = input("terceiro aluno: ")
aluno4 = input("quarto aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(lista)
