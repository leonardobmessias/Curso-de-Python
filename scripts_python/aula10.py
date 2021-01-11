#condicoes
"""tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('----FIM-----')"""
#segunda forma
"""tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo' if tempo <= 3 else ' Carro velho')
print('----FIM----')"""

#trabalhando com nome
"""nome = str(input('Qual seu nome? ')).capitalize()
if nome == 'Leonardo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))"""

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print('Sua media foi {:.1f}'.format(m))
print('PARABENS!!'  if m >= 6. else 'ESTUDE MAIS!')
'''if m >= 6.0:
    print('Sua media foi boa! PARABÉNS')
else:
    print('Sua media foi ruim! ESTUDE MAIS')'''