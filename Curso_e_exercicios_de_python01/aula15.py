# loop infinito
'''cont = 1
while True:
    print(cont, '->', end='')
    cont +=1
print('Acabouu')'''
n = s =  0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s +=n
#print('A soma vale {} '.format(s))
print(f'A soma vale{s}') #nova forma de escrever em python
#exemplos f'string
nome = 'Jose'
idade = 33
print(f'O {nome} tem {idade} anos.')