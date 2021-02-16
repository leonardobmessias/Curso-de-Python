idade = 0
contidade = contsexo= contmulher = 0
sexo = ''
escolha = ''
print(10 *'-','\nCADADASTRE UMA PESSOA\n', 10 * '-')
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        contidade +=1
    while True:
        sexo = str(input('Sexo[M/F]: ')).lower().strip()[0]
        if sexo == 'm':
            contsexo +=1
        if sexo  in 'mf':
            break
    while True:
        escolha = str(input('Quer continuar?[S/N] ')).lower().strip()[0]
        if escolha  in 'sn':
            break
    if sexo in 'f' and idade < 20:
        contmulher +=1
    if 'n' in escolha:
        break
print(f'O total de pessoas com mais de 18 anos é de {contidade}')
print(f'A quantidade de homens cadastrados é de {contsexo}')
print(f'Existem {contmulher} mmulheres com menos de 20 anos')