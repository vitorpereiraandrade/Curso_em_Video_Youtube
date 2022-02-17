# Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir
# qual foi o numero escolhido pelo computador.
# O programa deverá escrever na tela se o usuario venceu ou perdeu

import random
print('Computador pensando em um numero de 0 a 5...')
n = int(input('Digite um numero de 0 a 5 para adivinhar o numero que o computador escolheu: '))
s = random.randint(0, 5)
if n == s:
    print('Parabéns vc acertou !!!!!!!!')
else:
    print('Errouuuuuuu... tente outra vez')
