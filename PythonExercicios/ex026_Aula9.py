# Crie um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A"
# Em que posição ela aparece a primeira vez
# Em que posição aparece a ultima vez

frase = input('Digite uma frase qualquer: ').strip().upper()
letraa = frase.count('A')
print(f'A letra "A" aparece na frase {frase} {letraa} vezes')
posicao = frase.find('A') + 1
print(f'A primeira letra "A" aparece na posição {posicao}')
ultima = frase.rfind('A') + 1
print(f'A ultima letra "A" aparece na posicao {ultima}')



