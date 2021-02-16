from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), )
print('Os valores sorteados foram:', end='')
for n in numeros:
    print(n, end=' ')
print(f'\nO mair valor sorteado foi: {max(numeros)}')
print(f'O menos valor sorteado foi {min(numeros)}')