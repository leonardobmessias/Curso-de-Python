numero = 0
resp = ''
cont = 0
s = 0
teste = 'n'
maior = 0
menor = 0
while teste != resp:
    numero = int(input('Digite um numero: '))
    cont += 1
    while menor == 0:
        menor = numero
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero
    s = s + numero
    resp = str(input('Quer continuar?[S/N]')).lower()
print('Você digitou o total de {} números'.format(cont))
print('A media entre eles e de {}'. format(s / cont))
print('O maior numero digitado foi {} e o menor numero foi {}'.format(maior, menor))
print('Fim')