from time import  sleep
def contagem(a, b):
    numero = []
    print(f'Contagem de {a} até {b} de 1 em 1 ')
    for c in range(a, b+1):
        print(c,end=' ')
        sleep(0.5)
        numero.append(c)
    print()
    print('-=' * 20)
    print(f'Contagem de {b} até {a} de 2 em 2')
    for c in range (b,a,-2):
        print(c,end=' ')
        sleep(0.5)
    print(b - b)
    print('FIM!')
    print('-=' * 20)
    print('Agora é sua vez de personaliza  a contegem!')
    a = int(input('Início: '))
    b = int(input('Fim: '))
    c = int(input('Passo:'))
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        for i in range(a, b, c):
            print(i, end=' ')
        print('FIM!')
    if a > b:
        if c > 0:
            c = 0 - (c)
        for i in range(a, b, c):
            print(i, end=' ')
        if c < 0:
            for i in range(b,a, c):
                print(c, end=' ')
            print(b)
        print('Fim')
contagem(1,10)