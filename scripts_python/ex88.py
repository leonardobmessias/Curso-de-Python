from random import randint
from time import sleep
lista = []
listatot = []
cont = 0
print(5 * '-', 'JOGA NA MEGA SENA', 5 * '-')
resp = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0,resp):
    for c in range(0, 6):
        lista.append(randint(1, 60))
    listatot.append(lista[:])
    print(f'Jogo: {cont +1} : {listatot[cont]}')
    sleep(1)
    cont +=1
    lista.clear()
print(5 * '-=', 'BOA SORTE', 5 * '=-')
