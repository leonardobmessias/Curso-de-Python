matriz = [[1,2,3],[4,5,6],[7,8,9]]
pares = 0
soma = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite umm valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] %2 == 0:
            pares += matriz[l][c]
        if matriz[l][2] == matriz[l][c]:
            soma += matriz[l][c]
    print()
print(max(matriz[1]))
print(f'A soma dos numeros pares é {pares}')
print(f'O Resultado da soma da terceira coluna é igual a {soma}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')