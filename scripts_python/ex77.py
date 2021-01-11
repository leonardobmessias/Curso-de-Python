lista = 'casa' , 'filho', 'python', 'dinheiro', 'policia', 'amizade', 'curso', 'chefe', 'felicidade', 'ano' 'novo', 'historia', 'café'
for c in lista:
    print(f'\nNa palavra {c.upper()} temos: ',end='')
    for letra in c:
        if letra in 'aeiou':
            print(letra, end=' ')