# Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

from math import sin, cos, tan, radians
angulo = float(input('Informe um angulo para descobrir o seno, cosseno e tangente: '))
seno = sin(radians(angulo)) # vc tem que passar em radianos o angulo para achar o Seno
print(f'O angulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O angulo de {angulo} tem o COSSENO {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O angulo de {angulo} tem TANGENTE {tangente:.2f}')


