peso = float(input('Qual seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)
if imc < 18.5 :
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Você está no seu peso ideal !')
elif imc <= 30:
    print('Você está sobrepeso!')
elif imc <= 40:
    print('Você está obeso!')
elif imc > 40:
    print('Você está com obesidade morbida')
