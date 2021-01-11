frase = str(input('Digite um frase:')).lower().split()
frase = ('').join(frase)
frase1 = ''
frase2 = ''
cont = 0
for c in frase[:]:
    frase1 = frase1 + frase[cont]
    cont += 1
print('pausa...')
for c2 in range(cont-1, -1, -1):
        frase2 = frase2 + frase[c2]
print(frase1)
print(frase2)
if frase1 == frase2:
    print('A Frase digitada é um polidromo!')
else:
    print('A frase digitada não é um polidromo!')
