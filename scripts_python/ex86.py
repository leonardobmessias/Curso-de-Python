matriz = [[1,2,3],[4,5,6],[7,8,9]]
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite umm valor para [{l}, {c}]: '))


for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
