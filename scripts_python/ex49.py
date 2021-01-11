n = int( input('Digite um numero para saber a tabuada:'))
for c in range(0, 10 +1):
    s = c * n
    print('{} x {} = {}'.format(n, c, s))
print('Fim!')