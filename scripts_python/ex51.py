n = int(input('Digite o numero: '))
r = int(input('Digite a razão: '))
decimo = n + (10 - 1) * r
for c in range(n, decimo + r, r):
    print(c, end=' > ')