# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possiveis sobre ela

algo = input('Digite algo: ')
print(f'O tipo primitivo é {type(algo)}')
print(f'Só tem espaços {algo.isspace()} ')
print(f'É um numero {algo.isnumeric()}')
print(f'É alfabetico {algo.isalpha()}')
print(f'É alfanumerico {algo.isalnum()}')
print(f'Está em maiuscula? {algo.isupper()}')
print(f'Está em minuscula? {algo.islower()}')
print(f'Está capitalizada (A PRIMEIRA LETRA MAIUSCULA? {algo.istitle()}')
