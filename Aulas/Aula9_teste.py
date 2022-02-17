frase = 'Curso em Video Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])
print("""Texto é um conjunto de palavras e frases encadeadas que permitem interpretação e transmitem uma mensagem. 
É qualquer obra escrita em versão original e que constitui um livro ou um documento escrito. 
Um texto é uma unidade linguística de extensão superior à frase.""") # 3 aspas vai imprimi o texto inteiro

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)
print(frase.find('Video')) # Video esta na posicao 9
print(frase.lower().find('video'))
dividido = frase.split()
print(frase)
print(dividido[2])
print(dividido[0])
print(dividido[2][3]) # pega o dividido 2 e me mostre a letra 3

