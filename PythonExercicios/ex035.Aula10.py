# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas podem ou nao formar um triangulo.

r1 = int(input('Informe o comprimento da 1ª reta: '))
r2 = int(input('Informe o comprimento da 2ª reta: '))
r3 = int(input('Informe o comprimento da 3ª reta: '))
if r1 < (r2 + r3):
   print('Forma um triangulo')
if r2 < (r1 + r3):
    print('Forma um triangulo')
if r3 < (r1 + r2):
    print('Forma um triangulo')
else:
    print('Não forma um triangulo')
