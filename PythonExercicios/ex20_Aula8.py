# O mesmo professor do desafio anterior quer sortear a ordem de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
aluno1 = input('Informe o primeiro aluno: ').upper()
aluno2 = input('Informe o segundo aluno: ').upper()
aluno3 = input('Informe o terceiro aluno: ').upper()
aluno4 = input('Informe o quarto aluno: ').upper()

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print(f'A ordem para apresentar o trabalho é: {alunos}')

