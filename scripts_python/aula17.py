'''nu = (2, 9, 5, 1 ) #tupla
nu2 = [2, 9, 5,1]#lista
print(type(nu))
print(nu2)
print(type(nu2))
nu2.append(7) #adiciona o elemento declara na ultima posição
print(nu2)
nu2.sort()#organiza a lista
print(nu2)
nu2.sort(reverse=True)# ordena ao contrario
print(nu)
print(f'Essa lista tem {len(nu2)} Elementos')#mostra a quantidade de elementos
nu2.insert(2,0)# primeira condição mostra a posição a ultima o valor que vai ser adicionado
print(nu2)
nu2.pop()#elimina o ultimo valor
print(nu2)
nu2.append(1)
print(nu2)
nu2.pop(2)#elimina o numero que esta na variavel declarada
print(nu2)
nu2.insert(2,2)
print(nu2)
nu2.remove(2)#remove o primeiro valor o valor declarado
if 4 in nu2:
    num.remove(5)
else:
    print('Não encontrei o numero 4')'''
#----------------------------------------
'''valores =[]
for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')
print('Cheguei ao final da lista!')'''

a =[2, 3, 4 ,7]
b = a[:]#Não cria uma ligação mais sim uma copia da lista
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')