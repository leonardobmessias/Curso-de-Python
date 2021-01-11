from datetime import date
ano = date.today().year
cont = 0
for c in range(0,7):
    nasc = int(input('Qual a data do seu nascimento? '))
    if (ano - nasc) > 21 :
        cont = cont + 1
print('{} pessoas cadastradas são maior de idade'.format(cont))
