# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA' no nome

nome = input('Informe seu nome: ').title()
if 'Silva' in nome:
    print(f'O nome {nome} tem "Silva" ')
else:
    print(f'O nome {nome} NAO tem "Silva" ')


# OUTRA MANEIRA DE FAZER

n = str(input('Qual seu nome completo: ')).strip().title()
print('Seu nome tem Silva? {}'.format('Silva' in n))        # IN é um operador do Python
