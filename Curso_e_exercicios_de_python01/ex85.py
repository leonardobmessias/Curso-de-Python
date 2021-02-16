num = [[], []]
valor = 0
for c in range (0, 7):
  valor = int(input('Digite um numero: '))
  if valor %2 == 0:
      num[0].append(valor)
  else:
      num[1].append(valor)

print(f'Os valores pares digitados foram {sorted(num[0])}')
print(f'O valores impares digitados foram: {sorted(num[1])}')
