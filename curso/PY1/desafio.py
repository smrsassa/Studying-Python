import random
n1 = str(input('nome1'))
n2 = str(input('nome2'))
n3 = str(input('nome3'))
n4 = str(input('nome4'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print ('{}'.format(lista))
