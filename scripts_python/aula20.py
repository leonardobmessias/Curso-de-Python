"""def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-'* 30 )


titulo('Curso em video!')
"""
"""def contador(*num):
    tam = len(num)
    print(f' Recebi os valordes{num} e são ao todo {tam} numeros')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)"""

"""def dobra(lst):
    pos = 0
    while pos< len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)"""
def soma(* valores):
    print(valores)
    s = 0
    for num in valores:
        s += num
    print(f'Somando os {valores} temos a {s}')
soma(5, 2)
soma(2, 9, 4)