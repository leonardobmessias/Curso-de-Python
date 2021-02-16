cidade = input('Digite o nome da sua cidade: ')
cidade = cidade.split()

cidade = 'Santo' in cidade[0] or 'santo' in cidade[0]
print('sua cidade começa com santo?:{}'.format(cidade))