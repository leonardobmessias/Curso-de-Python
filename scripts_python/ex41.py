from datetime import date
ano_nascimento = int(input('Qual a data de seu nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade <= 9:
    print("Você tem {} anos, logo pertence ao time Mirim!".format(idade))
elif idade <= 14:
    print('Você tem {} anos, logo pertence ao  time Infantil!'.format(idade))
elif idade <= 19:
    print('VocÊ tem {} anos , logo pertence ao time Junior!'.format(idade))
elif idade<= 20:
    print('Você tem {} anos, logo pertence ao time Senior!'.format(idade))
elif idade > 20:
    print('Você tem {} anos, logo pertence ao time Master'.format(idade))