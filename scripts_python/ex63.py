qnt = int(input('Quantos numeros você quer ver? '))
print('Sequência de Fibonaci')
cont = 3
t1 = 0
t2 = 1
print('{} > {} >'.format(t1,t2))
while qnt >= cont:
    t3 = t2 + t1
    print('> {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont +=1