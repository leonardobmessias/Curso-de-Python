from random import randint
from time import sleep
computador = randint(0,10)
jogador = 11
contador = 0
while jogador != computador:
    jogador = int(input('Tente adivinhar o numero que pensei:'))
    print('...')
    sleep(0.5)
    contador +=1
    print("você disse {}...".format(jogador))
    if jogador != computador:
        print('Você errou! Tente novamente')
    else:
        print('Parabens você acertou!')
print('Pessei o numero {}'. format(computador))
print("Você precisou de {} chances para acertar".format(contador))
