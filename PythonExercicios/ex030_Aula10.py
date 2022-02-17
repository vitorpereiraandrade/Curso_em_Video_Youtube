# Crie um programa que leia um número inteiro e mostre se ele é PAR ou IMPAR

n = int(input('Digite um número: '))
impar = n / 2
if impar % 1:
    print(f'O número {n} é IMPAR')
else:
    print(f'O número {n} é PAR')