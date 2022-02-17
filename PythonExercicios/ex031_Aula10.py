# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas

d = float(input('Qual a distância da sua viagem: '))
if d <= 200:
    print(f'Sua viagem vai custar R${d * 0.50:.2f}')
else:
    print(f'Sua viagem vai custar R${d * 0.45:.2f}')