nota1 = float(input('Qual o valor da primeira nota? '))
nota2 = float (input('Qual o valor da segunda nota? '))
media = (nota1 + nota2) / 2
if media <= 5.0:
    print('Sua media é {:.1f}, você foi reprovado!'.format(media))
elif media > 5.1 and media < 6.9:
    print('sua media foi {:.1f} você está em recuperação!'.format(media))
else:
    print('Sua media é {:.1f}, você foi aprovado!'.format(media))