# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

ano = int(input('Informe um ano para saber se é Bissexto: '))
n = ano / 4
n1 = ano / 400
if n % 1 or n1 % 1:
    print(f'O ano de {ano} Nao é um ano Bissexto: ')
else:
    print(f'O ano de {ano} é um ano Bissexto')

