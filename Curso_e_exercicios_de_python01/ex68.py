from random import randint
computador = randint(1,10)
jogador = soma = cont = 0
escolha = ''
parouimpa = ''
print('Jogo de par ou impar!')
while True:
    jogador = int(input('Diga um valor:'))
    escolha = str(input('Você quer par ou impar?')).lower().strip()[0]
    soma = jogador + computador
    print(f'O computador escolheu {computador}')
    if soma % 2 == 0:
        parouimpa = 'p'
    else:
        parouimpa = 'i'

    if escolha != parouimpa:
        break
    else:
        cont +=1
print('Você perdeu')
print(f'Você venceu {cont} vezes!')

