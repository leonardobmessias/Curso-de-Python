l1 = float(input('Digite a primeira medida:'))
l2 = float(input('Digite a segunda medida:'))
l3 = float(input('Digite a terceira medida:'))
if l1 < ( l2 + l3) and l2 < (l1 + l3) and l3 < (l2 + l1):
    print('É possivel formar um triangulo')
else:
    print('Não é possivel formar um triangulo')
