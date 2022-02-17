# Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "santo"

cidade = input('Informe o nome de uma cidade: ').strip().title()
lista = cidade.split()
if 'Santo' in lista[0]:
    print(f'A cidade de {cidade} comeca com o nome SANTO')
else:
    print(f'A cidade de {cidade} não começa com o nome SANTO')


# OUTRA MANEIRA

cid = str(input('Em que cidade vc nasceu: ')).strip().title()
print(cid[:5] == 'Santo')
