import random
aposta = int(input('aposte um numero entre 0 e 5: '))
r = int(random.randint(0,5))
if aposta == r:
    print ('vc ganhou, parabens!')
else:
    print ('tente novamente, eu pensei no numero {}'.format(r))
print('Obrigado por participar')