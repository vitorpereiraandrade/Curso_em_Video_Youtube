nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é tão normal')
print(f'Bom dia, {nome}')
print('--FIM--')

# Outro
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) / 2
print(f'A sua média foi {m:.2f}')
if m >= 6.0:
    print('Sua média foi boa, parabéns')
else:
    print('Sua média foi ruim, estude mais')
