###tuplas são imutaveis
'''
lanche = ('Hanburguer', 'Suco', 'Batata', 'Pizza')
for c in lanche:
    print (c)
print ('-'*30)
for c in range (0, len(lanche)):
    print (lanche[c])
for p, c in enumerate(lanche):
    print (c)
    print (sorted(lanche))
'''
### del(lanche) apaga a variavel
'''
a = (5 ,8 ,4)
b = (4 ,3 ,2)
c = a + b
print (c)
print (c.index(8))
print (c.count(4))
'''
