lista = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Desessete', 'Dezoito', 'Dezenove', 'Vinte'
n = int(input('Digite um numero entre 0 e 20: '))
while True:
    if n in range(0, 21):
            break
    else:
        n = int(input('Numero invalido! Digite um numero ebtre 0 e 20: '))
print(f'Você digitou {lista[n]}...')