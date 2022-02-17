# Crie um programa que leia um numero Real qualquer pelo teclado e mostre a sua porcao Inteira.
# Ex. Digite um numero: 6.127 - O numero 6.127 tem a parte inteira 6.

from math import trunc
real = float(input('Digite um número Real: '))
print(f'O número {real} tem a parte inteira {trunc(real)}')