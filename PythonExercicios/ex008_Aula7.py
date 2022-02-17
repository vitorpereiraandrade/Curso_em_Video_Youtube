# Escreva um programa qie leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = float(input('Informe o valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print(f'{metros:.2f} metros tem:\n{centimetros:.0f} centimetros\n{milimetros:.0f} milimetros')