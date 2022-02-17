# Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
# EX: Ana Maria de Souza - Primeiro = Ana - ultimo Souza

nome = input('Informe seu nome completo: ').title()
lista = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome: {lista[0]}\nSeu ultimo nome: {lista[-1]}')
