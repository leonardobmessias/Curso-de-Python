from datetime import date #função pega a data atual do computador
ano = int(input("Digite uma ano  valido:"))
if ano == 0:
    ano = date.today().year # chama o ano
print('Ano bissesto' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'Não é um ano bissesto')
print(ano)
