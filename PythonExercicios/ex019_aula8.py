# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome escolhido.

from random import choice

aluno1 = input('Informe o nome do primeiro aluno: ').upper()
aluno2 = input('Informe o nome do segundo aluno: ').upper()
aluno3 = input('Informe o nome do terceiro aluno: ').upper()
aluno4 = input('Informe o nome do quarto aluno: ').upper()
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista)
print(f'O sorteado para apagar o quadro é:  {sorteio}')

