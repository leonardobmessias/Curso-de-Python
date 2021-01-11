dados= {}
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input('Média: '))
print(f'O nomer é igual a {dados["nome"]}')
print(f'A média é igual a {dados["media"]}')
if dados['media'] >= 7:
    print('A situação é igual a Aprovado!')
elif dados['media'] < 7 and dados['media'] >= 6 :
    print('Asituação é de Recuperação!')
else:
    print('A situação é igual a Reprovado!')
