from datetime import date
ano_nasc = int(input('Qual o ano de seu nascimento? '))
ano_atual = date.today().year
if (ano_atual - ano_nasc) < 18 :
    print('Não está na hora de se faltan {} anos!'.format((ano_nasc - ano_atual) - 18))
elif (ano_atual - ano_nasc) == 18 :
    print('Esse é o ano que você deve se alistar!')
else:
    print('Já passou da data do seu alistamento em {} anos'. format((ano_atual - ano_nasc) - 18))

