n = int(input('Digite um numero:'))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print(c, end=' ')
        tot += 1
print('O numero {} foi dividido {} vezes'.format(n, tot))
if tot == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')