ano = int(input('digite o ano desejado: '))
bi = ano%4
if bi == 0:
    print ('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é bissexto!'.format(ano))