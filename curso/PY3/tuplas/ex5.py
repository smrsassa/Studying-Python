###exercicio 76
produtos = ('lapis', 1.5, 'borracha', 2.00, 'caderno', 15.00, 'livro', 50.00, 'mochila', 75.00)
print ('='*60)
print ('{:^60}'.format('Lista de produtos'))
print ('='*60)
for c in range (0, len(produtos), 2):
    print ('{:<50}R$ {:>7}'.format(produtos[c], produtos[c+1]))
print ('-'*60)