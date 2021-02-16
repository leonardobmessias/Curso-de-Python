#tuplas
#tuplas são imutaveis
'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)# mostra a tupla inteira
print(lanche[1]) #corresponde  posição 1. Sabendo que a contagem começa na posição 0. o vetor 1 que é igual a suco
print(lanche[3])#pudim
print(lanche[-2]) # De tras para frente printa o elemento pizza
print(lanche[1:3])#mostra do elemento 1 ao 3. Sabendo que o numero 3 sera ignorado. Então apararecera Suco=1 e pizza=2
print(lanche[2:])#mostra do elemento 2 = pizza até o final
print(lanche[:2])#mostra do inicio até a variavel 2 desconsiderando o numero 2= printará so hamburguer e suco
print(sorted(lanche))# mostra a cariavel lanche em ordem, sem alterar a natural
for c in lanche:
    print(f' Eu vou comer {c}')
print('-----mostrando com contador-----')
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')
print("-----modo com enumerate-----")
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c) #ajunta a tupla 'a' coma tupla 'b'
print(len(c))
print(c.count(5))#quantas vezes aparecem o numero declarado no caso o 5 aparece 2 vezes
print(c.index(4))# mostra a posição do numero declarado no caso seria o numero 6 (5, 8, 1, 2, 2, 5, "4"posição 6)
print(c.index(5,1))#apresenta o numero apartir da posição deslocada

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)