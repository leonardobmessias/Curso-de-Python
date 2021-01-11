import random
from time import sleep
n = int(input('Digite um numero:'))
s = random.randint(0,5)
print("PROCESSANDO..")
sleep(2)
if n == s :
    print('Você venceu!')
else:
    print("Você perdeu !Tente novamente!")
print(s)