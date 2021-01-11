from random import shuffle
nome1 = input('Qual o primeiro nome?')
nome2 = input('Qual o segundo nome?')
nome3 = input('Qual o terceito nome?')
nome4 = input('Qual o quarto nome?')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem de apresentação será{}'. format(lista))
