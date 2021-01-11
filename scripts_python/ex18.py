# Primeira forma, importando todo o modulo
"""import math
angulo = float(input('Qual o angulo?'))
seno = math.sin(math.radians(angulo))
print('O angulo {} tem o SENO de{:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo{} tem a TANGENTE  de {:.2f}'.format(angulo, tangente))"""

#Forma importando apenas a parte especifica do modulo
from math import sin, cos, tan, radians
angulo = float(input('Qual o angulo?'))
seno = sin(radians(angulo))
print('O angulo {} tem o SENO de{:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo{} tem a TANGENTE  de {:.2f}'.format(angulo, tangente))