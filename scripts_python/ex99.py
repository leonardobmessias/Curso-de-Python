from random import randint
def maior(*n):
    if len(n) != 0:
        print(f'Foram informados {len(n)} valores')
        print(f'O maior valor é igal a {max(n)}')
    else:
        print('Não foi passado nenhum parametro!')
    print()

maior(2, 9, 4, 5, 7,1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()