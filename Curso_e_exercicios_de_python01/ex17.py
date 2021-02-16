from math import hypot
cat_oposto = float(input('Digite o valor do cateto oposto:'))
cat_adijacente = float(input('Digite o valor do cateto adjacente'))
hipotenusa = hypot(cat_oposto,cat_adijacente)
print('A hipotenusa do triangulo é :{:.2f}'.format(hipotenusa))