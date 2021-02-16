s = n = cont = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999: break
    s += n
    cont += 1
print(f'O total de de numeros digitados foi {cont} e a soma entre eles e de {s}')