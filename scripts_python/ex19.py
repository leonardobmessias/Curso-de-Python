# Primeiro usando todo modulo  random
"""import random
nome1 = input('Qual o primeiro nome?')
nome2 = input('Qual o segundo nome?')
nome3 = input('Qual o terceiro nome?')
nome4 = input('Qual  o nome do quarto nome?')
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))"""
# Segundo modo usando apenas a caracteríscica choice de random
from random import choice
nome1 = input('Qual o primeiro nome?')
nome2 = input('Qual o segundo nome?')
nome3 = input('Qual o terceiro nome?')
nome4 = input('Qual  o nome do quarto nome?')
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))