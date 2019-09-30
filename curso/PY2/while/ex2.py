#exercicio 58
import random
aposta = int(input('aposte um numero entre 1 e 10: '))
r = int(random.randint(1,10))
if r == aposta:
    print ('Voce acertou de primeira!!!')
else:
    c = 1
    while r != aposta:
        aposta = int(input('aposte um numero entre 1 e 10: '))
        c += 1
print ('Voce precisou de {} tentativas para acertar o valor {}'.format(c, r))
print ('Fim!!!')

##exercicio 58 alternativo onde o pc tenta adivinhar a resposta
#import random
#aposta = int(input('aposte um numero entre 1 e 10: '))
#r = int(random.randint(1,10))
#if r == aposta:
#    print ('O computador acertou de primeira')
#else:
#    c = 2
#    while r != aposta:
#        r = int(random.randint(1,10))
#        if r == aposta:
#            print ('O computador precisou de {} tentativas para acertar'.format(c))
#        else:
#            c += 1
#print('Obrigado por participar')