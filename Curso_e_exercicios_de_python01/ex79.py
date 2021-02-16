lista = []
escolha =''
while True:
    n = (int(input('Digite um numero:''')))
    lista.append(n)
    if lista.count(n) > 1:
        while True:
            lista.pop()
            n = int(input('O numero já existe na lista! Digite um novo numero: '))
            lista.append(n)
            if lista.count(n) == 1:
                break
    escolha = str(input('Quer continuar? [SN]')).lower().strip()[0]
    if escolha in 'n':
        break
print(f'A lista armazenada foi {lista.sort()}')
