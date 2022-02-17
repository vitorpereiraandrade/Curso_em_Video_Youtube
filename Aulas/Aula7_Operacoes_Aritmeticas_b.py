print(81**(1/2)) # Raiz Quadrada
print('oi' * 5)
print('='*20)


nome = input('Qual o seu nome? ')
print(f'Ola {nome:20}!')
print(f'Ola {nome:>20}!') # 20 espacos a direita
print(f'Ola {nome:<20}!') # 20 espacos a esquerda
print(f'Ola {nome:^20}!') # centralizado a 20 espacos
print(f'Ola {nome:=^20}!')
print(f'Ola {nome:*^20}!\n') # centralizado a 20 espacos

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print(f'A soma vale {n1+n2}\n')

m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A multiplicacao é {m} e a divisao é {d:.2f}')
print(f'Divisao inteira é {di} a potência é {e}')
print(f'A multiplicacao é {m} e a divisao é {d:.2f}', end=' ') # Junta a linha debaixo
print(f'Divisao inteira é {di} a potência é {e}')
print(f'A multiplicacao é {m} e a divisao é {d:.2f}', end='>>>>>>') # Junta a linha debaixo mas com alguma caracter
print(f'Divisao inteira é {di} a potência é {e}')