import math
n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
if n1>n2 & n2<n3:
    print ('{} é o maior e {} o menor dos 3'.format(n1, n2))
elif n1>n2 & n3<n2:
    print ('{} é o maior e {} o menor dos 3'.format(n1, n3))
elif n2>n1 & n1<n3:
    print ('{} é o maior e {} o menor dos 3'.format(n2, n1))
elif n2>n1 & n3<n1:
    print ('{} é o maior e {} o menor dos 3'.format(n2, n3))
elif n3>n2 & n2<n1:
    print ('{} é o maior e {} o menor dos 3'.format(n3, n2))
else:
    print ('{} é o maior e {} o menor dos 3'.format(n3, n1))