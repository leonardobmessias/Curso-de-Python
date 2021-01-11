nome = input('Qual seu nome?')
print('Seu nome em letra maiusculas é {}'.format(nome.upper()))
print('Seu nome em letras minusculas é {}'.format(nome.lower()))
print( nome.title().strip())
nome = nome.split()
print('seu nome tem {} letras '.format(len(''.join(nome))))
print('Seu primeiro nome é {} e tem {} letras'.format(nome[0],len(nome[0])))

