sexo = ''
while sexo != 'M' and sexo != 'F':
   sexo = str(input('Digite seu sexo:[M/F]')).upper()
   if sexo != 'M' and sexo!= 'F':
       print('Por favor digite uma resposta valida!')
   elif sexo == 'M':
       print('Registramos que você é do sexo Masculino')
   elif sexo == 'F':
       print('Registramos  que você é do sexo feminino')
print('Fim')
#Forma guanabara
'''
sexo = str(input('Informe seu sexo:')).strip().upper()[0]
while sexo not in 'MmFf:
    sexo = str(input('Dados invalidos. Informe seu sexo')).strip().upper()[0]
prin('sexo {} regisrado'.format(sexo))
'''
