# Leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

s = float(input('Informe seu salario: R$ '))
aumento = s * 0.15
print(f'Um funcionario ganhava R${s:.2f}. Seu novo salario com aumento de 15% é de R${s + aumento:.2f}')