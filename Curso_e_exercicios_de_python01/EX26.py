frase = input('Digite uma frase: ').strip()

print('Sua frase tem {} letras A'.format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na {} posição'.format(frase.upper().find('A')+1))
print('A ultima vesz que ela apareceu foi {}'.format(frase.upper().rfind('A')+1))