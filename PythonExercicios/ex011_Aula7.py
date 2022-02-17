# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua Area e a quantidade de tinta
# necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m quadrados.

l = float(input('Qual a largura da parede: '))
a = float(input('Qual a altura da parede: '))
area = l * a
print(f'A area da parede é de {area:.2f} metros quadrados')
tinta = area / 2
print(f'Vc vai precisar de {tinta} litros de tinta para pintar sua parede')