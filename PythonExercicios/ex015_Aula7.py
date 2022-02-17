# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$ 60 por dia e R$0,15 por km rodado.

km = int(input('Qual a quantidade de Km rodados: '))
dias = int(input('Qual a quantidade de dias vc utilizou o veiculo: '))
valor_dias = dias * 60
valor_km = km * 0.15
print(f'Vc alugou seu veiculo por {dias} dias e rodou {km}km o preço total do aluguel é de R${valor_dias + valor_km:.2f}')