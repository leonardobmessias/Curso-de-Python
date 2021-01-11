pessoa = {}
grupo = []
somaidade = cont = 0
mulher = ''
acimamedia = {}
while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo[M/F]: '))
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    grupo.append(pessoa)
    if pessoa['sexo']  in 'Ff':
        mulher += ' ' + pessoa['nome']
    del pessoa
    cont +=1
    res = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    if res in 'n':
        break
print(grupo)
print(f'O grupo tem {cont} pessoas')
print(f'A média de idade é de {somaidade / cont}.')
print(f'As mulheres cadastradas foram {mulher}.')
media = somaidade / cont
print()
print('Lista de pessoas que estão com idade acima da media:')
for c,v in enumerate(grupo):
    if v['idade'] > media:
        print(f'nome = {v["nome"]}; sexo = {v["sexo"]}; idade = {v["idade"]} ')
