# Escreva um programa que leia a velocidade de uma carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.

v = int(input('Informe a velocidade do veiculo: '))
if v > 80:
    print(f'Sua velocidade é {v}km/h, vc ultrapassou o limite de velocidade, será multado no valor de R${(v-80) * 7}')
else:
    print('Parabéns, vc está no limite de velocidade')