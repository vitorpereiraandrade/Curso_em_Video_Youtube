tempo = int(input('Quantos anos tem seu carro: '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

# Linha simplificada
tempo2 = int(input('Quantos anos tem seu carro: '))
print('Carro novo' if tempo2 <= 3 else'Carro velho')
print('--FIM--')