s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 ==0:
        s += n
        cont +=1
print('O resultado da operação é : {} para a quantidade de {} numeros'.format(s,cont))