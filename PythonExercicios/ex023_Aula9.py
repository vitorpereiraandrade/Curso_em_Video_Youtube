# Faca um programa que leia um numero de 0 a 9999 e mostre cada uma dos digitos separados
# ex: Digite um numero: 1834
# Unidade: 4 - Dezena: 3 - Centena: 8 - Milhar 1

num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o numero {num}')
print(f'Unidade: {u} ')
print(f'Dezena: {d}')
print(f'Centena: {c} ')
print(f'Milhar: {m} ')
