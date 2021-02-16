#programa tabuada com saida em um numero negativo
n = cont = 1
while True:
    n = int(input('Você que ver a tabuada de qual valor? '))
    if n < 0: break
    cont = 1
    print(10 * '-')
    while True:
        print(f'{n} x {cont} = { n*cont }')
        cont +=1
        if cont > 10: break
    print(10 * '-')