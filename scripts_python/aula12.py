nome = str(input('Qual seu nome?'))
if nome == 'Leonardo':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome =='José':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jessica':
    print('Seu nome é feminio')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}!'.format(nome))
