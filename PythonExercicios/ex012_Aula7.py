# Leia o preco do produto e mostre seu novo preco com 5% de desconto

p = float(input('Qual o preço do produto: R$'))
desconto = p * 0.05
print(f'O preço do produto é R${p:.2f}, está na promoção com 5% de desconto fica R$ {p - desconto:.2f}')

outra_maneira = float(input('O preço R$'))
desconto_outra_maneira = outra_maneira - (outra_maneira * 5 / 100)
print(f'{desconto_outra_maneira:.2f}')