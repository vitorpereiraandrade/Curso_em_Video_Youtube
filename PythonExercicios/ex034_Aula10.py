# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

s = float(input('Qual o seu salário: R$ '))
if s <= 1250:
    print(f'Com aumento de 15% seu novo salário vai para R${(s * 0.15) + s:.2f}')
else:
    print(f'Com aumento de 10% seu novo salário vai para R${(s * 0.10) + s:.2f}')