#estutura com for
'''for c in range(1,10):
    print(c)
print('Fim')'''

# estrutura com while
#Whileé utilizado quando não sabemos a quantidade dos laços
'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''

#Flag condição de parada. o programa para quando for digitado '0'
'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''
r = 'S'
#flag solicitando se usuario deseja sair
'''while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar ? ')).upper()
print('Fim')'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par +=1
        else:
            impar +=1
print("Você digitou {} numeros pares e {} numeros impares".format(par, impar))