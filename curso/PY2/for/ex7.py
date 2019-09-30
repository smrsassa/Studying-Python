###exercicio 52
n = int(input('digite um numero: '))
if n == 2 or n == 3 or n == 5:
        print ('{} é um numero primo'.format(n))
elif n%2 == 0 or n%3 == 0 or n%5 == 0:
        print ('{} não é um numero primo'.format(n))
else:
        print ('{} é um numero primo'.format(n))
print ('Fim!!!')