nome = input('Digite seu nome: ').strip().title()
primeiro = nome.find(' ')
segundo = nome.rfind (' ')
print('Muito prazer em te conhecer, seu primeiro nome é {} e seu ultimo nome é {}'.format(nome[:primeiro], nome[segundo:]))