import random
print ('''Bem Vindo ao jokenpô\nAqui voce vai jogar contra o computador\n
Escolha pedra, papel, ou tesoura e veja o resultado!!!''')
print ('[0] para escolher pedra')
print ('[1] para escolher papel')
print ('[2] para escolher tesoura')
aposta = int(input('Digite aqui: '))
opc = ('pedra', 'papel', 'tesoura')
pcaposta = random.randint(0, 2)
if aposta == pcaposta:
    print ('Empate!')
    print ('O computador tambem escolheu {}'.format(opc[pcaposta]))
elif aposta == 0 and pcaposta == 1:
    print ('Voce perdeu!')
    print ('O computador escolheu {}'.format(opc[pcaposta]))
elif aposta == 0 and pcaposta == 2:
    print ('Voce venceu!')
    print ('O computador escolheu {}'.format(opc[pcaposta]))
elif aposta == 1 and pcaposta == 0:
    print ('Voce venceu!')
    print ('O computador escolheu {}'.format(opc[pcaposta]))
elif aposta == 1 and pcaposta == 2:
    print ('Voce perdeu!')
    print ('O computador escolheu {}'.format(opc[pcaposta]))
elif aposta == 2 and pcaposta == 1:
    print ('Voce venceu!')
    print ('O computador escolheu {}'.format(opc[pcaposta]))
elif aposta == 2 and pcaposta == 0:
    print ('Voce perdeu!')
    print ('O computador escolheu {}'.format(opc[pcaposta]))
print ('Obrigado por jogar!')
fim = input('Aperte qualquer tecla para finalizar...')
