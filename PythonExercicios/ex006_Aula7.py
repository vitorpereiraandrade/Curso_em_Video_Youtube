# Informe um numero e de o dobro, triplo e raiz quadrada

n = int(input('Informe um numero: '))
dobro = n * 2
triplo = n * 3
raiz = n **(1/2)
print(f'O dobro do numero é {dobro}\nTriplo {triplo}\nRaiz {raiz:.2f}')     # ou

print(f'O dobro do numero {n} é {n * 2}, o Triplo é {n * 3}, e a raiz quadrada é {n **(1/2):.2f}')
