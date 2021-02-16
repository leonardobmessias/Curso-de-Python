from datetime import date
ano = date.today().today().year
def votacao(nasc):
    idade = ano - nasc
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: O voto é OBRIGATORIO!'
    elif idade < 18 and idade >= 16 or idade > 65:
        return f'Com {idade} anos: o voto é OPCIONAL!'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
data = int(input('Em que ano você nasceu? '))
print(votacao(data))

