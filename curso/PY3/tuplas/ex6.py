###exercicio 77
tupla = ('Samuel', 'Rafaela', 'Evandro', 'Luciana')
vogais = ('a', 'e', 'i', 'o', 'u')
for c in range (0, len(tupla)):
    print ('\nA palavra {} tem as vogais'.format(tupla[c]), end=' ')
    for co in range (0, len(vogais)):
        if vogais[co] in tupla[c]:
            print ('{}'.format(vogais[co]), end=' ')