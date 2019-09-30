###exercicio 48
s = 0
for c in range (1, 500):
    if c%2 != 0 and c%3 == 0:
        s += c
print ('soma entre todos os numeros impares\nentre 1 e 500 é {}'.format(s))        
print ('Fim!!!')