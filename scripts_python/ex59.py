n1 = float(input('Digite o primeiro valor:'))
n2 = float(input('Digite o segundo valor:'))
escolha = 0
while escolha != 5:
    print('Faça sua escolha:')
    print('''
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR''')
    escolha = int(input())
    if escolha == 1:
        print('A soma dos numeros é igual a {}'.format(n1+n2))
    if escolha == 2:
        print('A Multiplicação dos numeros {} e {} é {}'.format(n1, n2, n1*n2))
    if escolha == 3:
        if n1 > n2:
            print('O numero maior é {}'.format(n1))
        elif n1 < n2:
            print('O maior numero é {}'.format(n2))
        else:
            print('Os numeros são iguais!')
    if escolha == 4:
        print('Digite novos números:')
        n1 = float(input('Digite o primeiro numero:'))
        n2 = float(input('Digite o segundo valor'))
print('Fim')
