medida1 = float(input('Informe a primeira medida: '))
medida2 = float(input('Informe a segunda medida: '))
medida3 = float(input('Informe a terceira medida: '))
triangulo = medida1 < medida2 + medida3 and medida2 < medida1 + medida3 and medida3 < medida1 + medida2
if triangulo is True:
    print('É possível formar um triângulo')
    if medida1 == medida2 and medida2 == medida3:
        print('O triangulo é equilatero')
    elif (medida1 == medida2 and medida2 != medida3) or (medida3 == medida2 and medida1 != medida3) or (medida1== medida3 and medida3 != medida2):
        print("o tringulo é isoceles")
    elif medida1 != medida2 and medida2 != medida3 and medida3 != medida1:
        print('O triangulo é escaleno')

else:
    print('Não é possivel formar um triangulo')