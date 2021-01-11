ctps = 0
salario = 0
dados= {}
from datetime import date
ano = date.today().year
print(ano)
while True:
    dados['nome']= str(input('Nome: '))
    dados ['idade'] = (ano - int(input('Data de nascimento: ')))
    dados['ctps'] = ctps = int(input('Carteira de trabalho (0 igual a não tem): '))
    if ctps == 0:
        break
    else:
        dados['anocont'] = int(input('Ano de contratação: '))
        dados['salario'] = salario = float(input('Salário: '))
        dados['aposentadoria'] = ((dados['anocont'] + 35) - (ano - dados['idade']))
        if salario > 0:
            break
print(dados)
print('----DADOS CADASTRADOS----')
for c, v in dados.items():
    print(f'{c} tem o valor {v}')