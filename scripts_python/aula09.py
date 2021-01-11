#caddeias de string
frase = 'curso em video python'
print(frase[9])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
"""# análise
print(len(frase)) # mostra o cumprimento
print(frase.count('o')) # conta quantas vezes a strin selecionada aparece
print(frase.count('o',0,13))# conta somente no fatiamento
print(frase.find('deo')) # mostra aonde começa a variavel declarada
print(frase.find('android')) # retorna um valor 'menos um' quando não há a variavel declarda
print('curso' in frase)

#transformação
print(frase.replace('python', 'androoid')) #substitui a primeira variavel pela segunda
print(frase.upper()) # Texto em caixa alta
print(frase.lower()) # Frase em caixa baixa
print(frase.capitalize()) #Torna a primeira letra da string em letra maiuscula
print(frase.title()) # Faz com que todas primeiras letras da palavra em maiuscula

frase = '   Aprenda Python  '
print(frase)
print(frase.strip())# retira os espaços inuteis
print(frase.rstrip())# tira os espaços da direita
print(frase.lstrip()) # tira os espaços esquerdo da palavra

frase = 'Curso em Video Python'
print(frase.split()) # Divide as palavras por padrão em espaço(cada palavra é colocada em uma nova lista)
frase = frase.split()
print(frase)
frase = '-'.join(frase) # ajunta a frase com o caractere selecionado
print(frase)"""

frase = 'Curso em Video Python'
dividido =frase.split()
print(dividido[2][3])