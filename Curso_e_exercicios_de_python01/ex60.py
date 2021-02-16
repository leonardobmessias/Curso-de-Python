n = int(input('Digite um numero para saber seu Fatorial'))
c = n
f = 1
print('Qualculando fatorial de {}'.format(n))
while c > 0:
    print('{} '.format(c), end=' ')
    print(' x ' if c >1 else ' = ',end= ' ')
    f = f * c
    c -=1
print(f)
'''from math import factorial
n = int(input('Digite um numero:'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))'''