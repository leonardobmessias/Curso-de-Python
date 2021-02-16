from datetime import date
ano = date.today().today()
print(ano)
def votacao(idade):
    if idade >= 18:
        print(f'Com {idade} anos: O voto é OBRIGATORIO!')
    elif idade < 18 and >= 16:
        print(f'Com {idade} anos: o voto é OPCIONAL!')
    elif idade > 16:
        print(f'Com {idade} anos: NÃO VOTA')
