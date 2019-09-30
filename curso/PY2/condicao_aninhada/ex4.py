idade = int(input('digite sua idade: '))
if idade < 18:
    tf = 18 - idade
    print ('Ainda não é hora de fazer o alistamento')
    print ('O alistamento será necessario daqui {} anos'.format(tf))
elif idade == 18:
    print ('Esta na hora de se alistar')
else:
    tf = idade - 18
    print ('Passou do tempo para se alistar')
    print ('Voce esta {} anos atrasado'.format(tf))
print ('Alistar-se é importante')