""""teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
#quando você adiciona uma lista sem fazer uma copia
#galera.append(teste) #lista sem copia
galera.append(teste[:])#lista com copia
print(galera) # uma lista dentro de uma lista
#quando eu altero a variavel teste eu sub escrevo  tambem a variavel galera
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
#para isso não acontecer é preciso fazer uma copia usando"""

"""galera = [['João', 15],['Ana',33],['Joaquim', 13],['Maria', 45]]
print(galera)
print(galera[0])#dados joão
print(galera[0][0])#so o nome de joão
print(galera[2][1])#idade joaquim

for p in galera: #dados completos dentro da lista
    print(p)
for p in galera:
    print(p[0]) #So os nomes"""
galera = list()
dados = list()
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])#necessario copia da lista e não alista em si
    dados.clear()#limpa a lista
print(galera)
for p in galera:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade')