###exercicio 51
t = int(input('digite um numero: '))
r = int(input('digite a razão da PA: '))
décimo = t + (11 - 1) * r
for c in range (t, décimo, r):
        print ('{}'.format(c), end=' - ')
print('Fim!!!')