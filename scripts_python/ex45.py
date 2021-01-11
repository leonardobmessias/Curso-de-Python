from random import randint
from time import sleep
computador = randint(1,3)
escolha = input('Escolha entre , pedra, papel ou tesoura:').lower().strip()
print(10 * '=', 'JOQUENPÔ', 10 * '=')
sleep(0.5)
if computador == 1:
    computador = 'pedra'
elif computador == 2:
    computador = 'papel'
elif computador == 3:
    computador = 'tesoura'


print('Você escolheu {} e o o computador {}'.format(escolha, computador))
sleep(1)
if computador == 'pedra'  and  escolha == 'tesoura':
    print('Pedra quebra tesoura, Você perdeu')
elif computador == 'pedra' and escolha =='papel':
    print('Papel embrulha pedra , você venceu!')
elif computador == 'tesoura' and escolha == 'pedra':
    print('Pedra quebra tesoura, Você venceu!')
elif computador == 'tesoura' and escolha == 'papel':
    print('Tesoura corta papel, você perdeu!')
elif computador == 'papel' and escolha == 'tesoura':
    print('Tesoura corta papel, Você venceu!')
elif computador == 'papel' and escolha == 'pedra':
    print('Papel embrulha pedra, você perdeu!')
elif computador == escolha:
    print('Que coisa! Deu empate')
