numero = 0
s = 0
numero = int(input('Digite um número [999 para parar]'))
while numero != 999:
    s = numero + s
    numero = int(input('Digite um número [999 para parar]'))
print('A soma estre os numeros foi  {}'.format(s))
print('Fim')