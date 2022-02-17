# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Informe seu nome completo: ')).strip()
print(f'O nome com todas letras maiuscula {nome.upper()}')
print(f'O nome com todas letras minuscula {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')



