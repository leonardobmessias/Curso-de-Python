lista = []
escolha = ''
n = 0
while True:
    lista.append(int(input('Digite um numero:')))

    escolha = str(input('Quer continar?[s/n]')).strip().lower()[0]
    if escolha in 'n':
        break
print(lista)
print(sorted(lista,reverse=True))
print(f'Foran digitados {len(lista)} numeros')
print( f'O numero 5 foi digitado {lista.count(5)}'if lista.count(5) > 0 else  'O numero 5 não pertence a lista' )
